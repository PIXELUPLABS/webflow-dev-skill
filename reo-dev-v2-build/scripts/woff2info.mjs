import fs from 'node:fs';
import zlib from 'node:zlib';
const KNOWN = ['cmap','head','hhea','hmtx','maxp','name','OS/2','post','cvt ','fpgm','glyf','loca','prep','CFF ','VORG','EBDT','EBLC','gasp','hdmx','kern','LTSH','PCLT','VDMX','vhea','vmtx','BASE','GDEF','GPOS','GSUB','EBSC','JSTF','MATH','CBDT','CBLC','COLR','CPAL','SVG ','sbix','acnt','avar','bdat','bloc','bsln','cvar','fdsc','feat','fmtx','fvar','gvar','hsty','just','lcar','mort','morx','opbd','prop','trak','Zapf','Silf','Glat','Gloc','Feat','Sill'];
function b128(buf, o) { let v = 0; for (let i = 0; i < 5; i++) { const b = buf[o.p++]; v = (v << 7) | (b & 0x7f); if (!(b & 0x80)) return v >>> 0; } throw new Error('bad b128'); }
for (const file of process.argv.slice(2)) {
  const buf = fs.readFileSync(file);
  const numTables = buf.readUInt16BE(12);
  const o = { p: 48 }; const tables = [];
  for (let i = 0; i < numTables; i++) {
    const flags = buf[o.p++]; const idx = flags & 0x3f; const ver = (flags >> 6) & 3;
    let tag = idx === 63 ? buf.toString('latin1', o.p, o.p + 4) : KNOWN[idx]; if (idx === 63) o.p += 4;
    const origLength = b128(buf, o);
    let transformed = (tag === 'glyf' || tag === 'loca') ? ver === 0 : ver !== 0;
    let len = origLength; if (transformed) len = b128(buf, o);
    tables.push({ tag, len });
  }
  const totalCompressed = buf.readUInt32BE(20);
  const data = zlib.brotliDecompressSync(buf.subarray(o.p, o.p + totalCompressed));
  let off = 0; const T = {};
  for (const t of tables) { T[t.tag] = data.subarray(off, off + t.len); off += t.len; }
  const out = { file: file.split('/').pop(), tables: tables.length };
  if (T['OS/2']) out.usWeightClass = T['OS/2'].readUInt16BE(4);
  if (T.fvar) {
    const f = T.fvar; const axOff = f.readUInt16BE(4), n = f.readUInt16BE(8), sz = f.readUInt16BE(10);
    out.axes = [];
    for (let i = 0; i < n; i++) { const b = axOff + i * sz; out.axes.push({ tag: f.toString('latin1', b, b + 4), min: f.readInt32BE(b + 4) / 65536, def: f.readInt32BE(b + 8) / 65536, max: f.readInt32BE(b + 12) / 65536 }); }
  }
  if (T.name) {
    const n = T.name; const count = n.readUInt16BE(2), strOff = n.readUInt16BE(4); const names = {};
    for (let i = 0; i < count; i++) { const r = 6 + i * 12; const pid = n.readUInt16BE(r), nid = n.readUInt16BE(r + 6), len = n.readUInt16BE(r + 8), so = n.readUInt16BE(r + 10);
      if (pid === 3 && [1, 2, 4, 16, 17].includes(nid) && !names[nid]) { const s = n.subarray(strOff + so, strOff + so + len); let str = ''; for (let k = 0; k < s.length; k += 2) str += String.fromCharCode(s.readUInt16BE(k)); names[nid] = str; } }
    out.names = names;
  }
  if (T.cmap) out.hasArrow2192 = 'unchecked';
  console.log(JSON.stringify(out));
}
