import json, subprocess, sys
spec = json.load(open(sys.argv[1]))
args = ['curl', '-sS', '-o', '/dev/null', '-w', '%{http_code}', spec['url']]
for k, v in spec['fields'].items():
    args += ['-F', f'{k}={v}']
args += ['-F', f"file=@{sys.argv[2]};type=font/woff2"]
print(sys.argv[2].split('/')[-1], '->', subprocess.run(args, capture_output=True, text=True).stdout)
