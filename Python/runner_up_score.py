n = int(input())
ar = list(map(int, input().split()))
mx = max(ar)
while max(ar) == mx:
    ar.remove(max(ar))
print(max(ar))
