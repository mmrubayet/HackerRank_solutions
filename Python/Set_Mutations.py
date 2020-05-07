n = int(input())
ar = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    arg = s[1:]
    if cmd !="print":
        eval('ar.{0}{1}'.format(cmd,tuple(map(int,arg))))
    else:
        print(ar)
