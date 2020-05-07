import re
n = int(input())

for i in range(n):
    a = input()
    x = bool(re.search('^[+-]?[0-9]*\.[0-9]+$', a))
    print(x)
