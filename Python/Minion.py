s = input()
vowels = 'AEIOU'

ks = 0
ss = 0
for i in range(len(s)):
    if s[i] in vowels:
        ks += (len(s)-i)
    else:
        ss += (len(s)-i)


if ks > ss:
    print("Kevin", ks)
elif ks < ss:
    print("Stuart", ss)
else:
    print("Draw")
