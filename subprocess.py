import subprocess
result = subprocess.run(['adb', 'shell', 'ls', '/'], stdout=subprocess.PIPE)
for x in result.stdout.decode('utf-8').splitlines():
    print(x)
