for t in range(int(input())):
    input()
    ls = [int(i) for i in input().split()]
    ml = ls.index(min(ls))
    l = ls[:ml]
    r = ls[ml+1:]
    if l == sorted(l,reverse=True) and r == sorted(r):
        print("Yes")
    else:
        print("No")
