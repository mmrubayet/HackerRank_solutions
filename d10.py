num = int(input())
count = 0
max = 0
while num > 0:
    if num % 2 == 1:
        count += 1
        if count > max:
            max = count
    else:
        count = 0
    num //= 2
print(max)
