n, m = map(int, input().split())
ar = list(map(int, input().split()))
sa = set(map(int, input().split()))
sb = set(map(int, input().split()))
h = 0
for i in range(n):
    if ar[i] in sa:
        h += 1
    if ar[i] in sb:
        h -= 1
print(h)
