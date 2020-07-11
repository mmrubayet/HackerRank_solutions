def pickingNumbers(a):
    return max([sum((a.count(i), a.count(i+1))) for i in set(a)])

n = int(input().strip())
a = list(map(int, input().rstrip().split()))
result = pickingNumbers(a)

print(result)
