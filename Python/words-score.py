n = int(input())
ns = list(map(str, input().split(' ')))
cn = 0
for i in ns:
    c=0
    for j in range(len(i)):
        if i[j] in 'aeiouy':
            c += 1
    if c%2==0:
        cn += 2
    else:
        cn += 1

print(cn)
