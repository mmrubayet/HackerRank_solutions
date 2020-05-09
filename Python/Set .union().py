_, a = input(), set(map(int, input().split()))
_, b = input(), set(map(int, input().split()))

print(len(list(a.union(b))))
