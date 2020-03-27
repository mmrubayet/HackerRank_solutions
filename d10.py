def decimalToBinary(n, nl=[]):
    if(n > 1):
        decimalToBinary(n//2)
    nl.append(n%2)
    return nl
dec = int(input())
bin = decimalToBinary(dec)
count = 0
max = 0
for num in bin:
    if num == 1:
        count += 1
        if count > max:
            max = count
    if num == 0:
        count = 0
ans = max
print(ans)
