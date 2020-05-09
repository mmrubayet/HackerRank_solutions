n = int(input())
sa = set(map(int, input().split()))
np = int(input())

for _ in range(np):
    s = input().split()
    cmd = s[0]
    nn = s[1]
    na = set(map(int, input().split()))
    eval('sa.{0}({1})'.format(cmd, na))

print(sum(list(sa)))
