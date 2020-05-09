n = int(input())
st = set(map(int, input().split()))
nc = int(input())

for _ in range(nc):
    s = input().split()
    cmd = s[0]
    arg = s[1:]
    eval('st.{0}{1}'.format(cmd,tuple(map(int,arg))))

print(sum(list(st)))
