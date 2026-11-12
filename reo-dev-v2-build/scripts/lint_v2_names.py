#!/usr/bin/env python3
"""Lint Webflow style names for the Reo.dev V2 build.

Two uses:

  1. Check a full style dump from the Webflow MCP against the legacy baseline:

       python3 lint_v2_names.py <get_styles_dump.json> [--baseline assets/legacy-style-baseline.json]

     The dump is the result of data_style_tool > get_styles {query: "all"} (the
     harness usually saves it to a file because it is large). Any JSON shape is
     accepted as long as it contains style objects with "id", "name" and
     "selector" / "isComboClass".

     Every style whose id is not in the baseline is treated as created after the
     audit and must follow the V2 naming rules.

  2. Check names before you send them (WHTML classes, create_style names):

       python3 lint_v2_names.py --names v2-hero_component is-secondary "v2-button is-dark"

     A quoted group is one element's class list: first the base, then combos.

  --list           also print every v2 class grouped by folder (for the daily review).
  --post-cleanup   after the cleanup runbook: no v2- names may remain.

Exit code 0 = clean, 1 = violations, 2 = usage error.
"""
import argparse
import json
import os
import re
import sys

BASE_RE = re.compile(r"^v2-[a-z0-9]+(-[a-z0-9]+)*(_[a-z0-9]+(-[a-z0-9]+)*)?$")
COMBO_RE = re.compile(r"^is-[a-z0-9]+(-[a-z0-9]+)*$")
CLEAN_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*(_[a-z0-9]+(-[a-z0-9]+)*)?$")
RESERVED_COMBOS = {
    "is-error", "is-label", "is-no", "is-partial", "is-reodev",
    "is-section", "is-value", "is-warning", "is-yes",
}
# Version markers are only a problem as a suffix: "-new", "-copy", "-2".
VERSION_WORDS = re.compile(r"[-_](new|copy|final|old|revamped|rewamped|temp|tmp)$|-\d$")
# Names that legitimately end in a digit.
ALLOWED_NUMERIC_TAIL = re.compile(r"(z-index-\d|-h[1-6]|-col-\d|-span-\d|-order-\d)$")


def check_base(name):
    problems = []
    if not name.startswith("v2-"):
        problems.append("missing v2- prefix")
        return problems
    if not BASE_RE.match(name):
        if name != name.lower():
            problems.append("uppercase letters")
        if name.count("_") > 1:
            problems.append("more than one underscore")
        if re.search(r"[^a-z0-9_-]", name.lower()):
            problems.append("characters other than a-z, 0-9, hyphen, underscore")
        if not problems:
            problems.append("does not match v2-[folder]_[element] / v2-[utility]")
    tail = name[3:]
    if VERSION_WORDS.search(tail) and not ALLOWED_NUMERIC_TAIL.search(tail):
        problems.append("version word or numeric suffix in the name (the prefix is the only version marker)")
    return problems


def check_combo(name):
    problems = []
    if name in RESERVED_COMBOS:
        problems.append("reserved: a legacy global class has this name")
    elif not COMBO_RE.match(name):
        problems.append("combo classes must be is-[variant], lowercase, hyphenated")
    return problems


def find_styles(node, out):
    if isinstance(node, dict):
        if "id" in node and "name" in node and ("selector" in node or "isComboClass" in node):
            out.append(node)
        else:
            for v in node.values():
                find_styles(v, out)
    elif isinstance(node, list):
        for v in node:
            find_styles(v, out)
    elif isinstance(node, str) and node[:1] in "[{":
        try:
            find_styles(json.loads(node), out)
        except ValueError:
            pass


def base_of(style):
    sel = style.get("selector") or ""
    m = re.match(r"^\.([^.\s:]+)", sel)
    return m.group(1) if m else None


def lint_dump(path, baseline_path, post_cleanup, show_list=False):
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    try:
        data = json.loads(raw)
    except ValueError:
        print("error: %s is not JSON" % path, file=sys.stderr)
        return 2
    styles = []
    find_styles(data, styles)
    if not styles:
        print("error: no style objects found in %s" % path, file=sys.stderr)
        return 2

    baseline = {}
    if baseline_path and os.path.exists(baseline_path):
        with open(baseline_path, encoding="utf-8") as fh:
            baseline = json.load(fh).get("styles", {})
    elif not post_cleanup:
        print("warning: baseline not found, every non-v2 class will be listed as unknown", file=sys.stderr)

    violations, unknown, v2_count, legacy_missing = [], [], 0, 0
    v2_bases, v2_combos = set(), {}
    seen = set()
    for s in styles:
        sid, name = s["id"], s["name"]
        seen.add(sid)
        is_tag = s.get("type") == "tag"
        is_combo = bool(s.get("isComboClass"))
        if post_cleanup:
            if is_tag:
                continue
            if name.startswith("v2-") or ".v2-" in (s.get("selector") or ""):
                violations.append((s.get("selector") or name, "v2- name still present after cleanup"))
            elif not is_combo and not CLEAN_RE.match(name):
                violations.append((s.get("selector") or name, "not a valid Client-First name"))
            continue
        if sid in baseline:
            continue
        if is_tag:
            unknown.append((s.get("selector") or name, "new tag / nested-tag style (V2 must not create or edit tag styles through the MCP)"))
            continue
        if is_combo:
            base = base_of(s)
            if base and base.startswith("v2-"):
                v2_count += 1
                v2_combos.setdefault(base, set()).add(name)
                for p in check_combo(name):
                    violations.append((s.get("selector") or name, p))
            else:
                unknown.append((s.get("selector") or name, "new combo on a non-v2 base"))
            continue
        if name.startswith("v2-"):
            v2_count += 1
            v2_bases.add(name)
            for p in check_base(name):
                violations.append((name, p))
        else:
            unknown.append((name, "new class without the v2- prefix"))

    if baseline and not post_cleanup:
        legacy_missing = sum(1 for sid in baseline if sid not in seen)

    print("styles in dump: %d" % len(styles))
    if not post_cleanup:
        print("v2 styles: %d" % v2_count)
        print("legacy styles no longer present: %d%s" % (
            legacy_missing,
            "  <- expected 0 before cleanup; if the V2 build removed any, tell the lead" if legacy_missing else ""))
    if violations:
        print("\nVIOLATIONS (%d) - fix these:" % len(violations))
        for name, why in sorted(set(violations)):
            print("  %-48s %s" % (name, why))
    if unknown:
        print("\nNOT IN BASELINE AND NOT V2 (%d) - yours: rename or remove. The client's own legacy work: leave it and tell the lead:" % len(unknown))
        for name, why in sorted(set(unknown)):
            print("  %-48s %s" % (name, why))
    if not violations and not unknown:
        print("\nOK: no naming violations.")
    if show_list and not post_cleanup:
        folders = {}
        for name in v2_bases:
            tail = name[3:]
            folder = tail.split("_")[0] if "_" in tail else "(global utilities and components)"
            folders.setdefault(folder, []).append(name)
        print("\nV2 CLASSES BY FOLDER (%d classes, %d folders):" % (len(v2_bases), len(folders)))
        for folder in sorted(folders, key=lambda f: (f.startswith("("), f)):
            print("  %s  [%d]" % (folder, len(folders[folder])))
            for name in sorted(folders[folder]):
                combos = sorted(v2_combos.get(name, []))
                print("    %s%s" % (name, ("   + " + ", ".join(combos)) if combos else ""))
        orphans = sorted(b for b in v2_combos if b not in v2_bases)
        if orphans:
            print("  combos whose base class is missing from the dump: %s" % ", ".join(orphans))
    return 1 if (violations or unknown) else 0


def lint_names(groups):
    bad = 0
    for group in groups:
        parts = group.split()
        if not parts:
            continue
        base, combos = parts[0], parts[1:]
        if base.startswith("is-") and not combos:
            problems = check_combo(base)
        else:
            problems = check_base(base)
            for extra in combos:
                if extra.startswith("v2-"):
                    problems += ["%s: %s" % (extra, p) for p in check_base(extra)]
                else:
                    problems += ["%s: %s" % (extra, p) for p in check_combo(extra)]
        if problems:
            bad += 1
            print("FAIL  %-44s %s" % (group, "; ".join(problems)))
        else:
            print("ok    %s" % group)
    return 1 if bad else 0


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description="Lint Reo.dev V2 style names.")
    ap.add_argument("dump", nargs="?", help="JSON file with the get_styles result")
    ap.add_argument("--baseline", default=os.path.join(here, "..", "assets", "legacy-style-baseline.json"))
    ap.add_argument("--names", nargs="+", help="class names or quoted class lists to check")
    ap.add_argument("--post-cleanup", action="store_true")
    ap.add_argument("--list", action="store_true", help="print every v2 class grouped by folder")
    args = ap.parse_args()
    if args.names:
        return lint_names(args.names)
    if not args.dump:
        ap.print_usage(sys.stderr)
        return 2
    return lint_dump(args.dump, args.baseline, args.post_cleanup, args.list)


if __name__ == "__main__":
    sys.exit(main())
