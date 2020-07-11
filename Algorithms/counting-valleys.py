def countingValleys(n, s):
    lc = 0
    vc = 0
    for i in range(n):
        if s[i] == 'U':
            lc += 1
        if s[i] == 'D':
            lc -= 1
        if lc == 0 and s[i] == 'U':
            vc += 1
    return vc

n = int(input())
s = input()

print(countingValleys(n, s))
