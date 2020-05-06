num = int(input())
count = 0
maxo = 0
while num > 0:
    if num % 2 == 1:
        count += 1
        maxo = max(maxo, count)
    else:
        count = 0
    num //= 2
print(maxo)
