a = list(map(int, input().strip().split(' ')))
e = list(map(int, input().strip().split(' ')))
f=0
if e[2]<a[2]:
    f = 10000
elif e[2]==a[2]:
    if e[1]<a[1]:
        f = (a[1]-e[1])*500
    elif e[1]==a[1] and e[0]<a[0]:
        f = (a[0]-e[0])*15

print(f)
