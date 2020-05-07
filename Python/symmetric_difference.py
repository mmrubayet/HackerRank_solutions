_, a = input(), set(map(int, input().split()))
_, b = input(), set(map(int, input().split()))

s = list(a^b)
s.sort()
print(*s, sep='\n')
