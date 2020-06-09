def kangaroo(x1, v1, x2, v2):
    con = 'NO'
    if (x2>x1 and v2>v1) or v1==v2:
        con = 'NO'
        print('0')
    if x2==x1 and v1==v2:
        con = 'YES'
        print('10')
    elif (x1 - x2) % (v2 - v1) == 0:
        con = 'YES'
        print('11')
    return con

X1V1X2V2 = input().split()

x1 = int(X1V1X2V2[0])

v1 = int(X1V1X2V2[1])

x2 = int(X1V1X2V2[2])

v2 = int(X1V1X2V2[3])

result = kangaroo(x1, v1, x2, v2)

print(result)
