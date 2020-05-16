import re
n = int(input())
for i in range(n):
    c = 'NO'
    if re.match(r'[789]\d{9}$', input()):
        c = 'YES'
    print(c)
