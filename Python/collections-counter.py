from collections import Counter
x = int(input())
stock = Counter(map(int, input().split()))
n = int(input())

income = 0

for i in range(n):
    size, price = map(int, input().split())
    if stock[size]:
        income += price
        stock[size] -= 1

print(income)
