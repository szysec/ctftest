import re

with open('tmp', 'rb') as f:
    c = f.read().decode()
    for i in range(-50, 50):
        print(''.join([chr(int(_)+i) for _ in re.findall('ICMP (\d+) Echo', c)]))
