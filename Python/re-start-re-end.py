import re
a=input()
b=input()
pattern = re.compile(b)
l = pattern.search(a)
if l:
    while l:
        print("({0}, {1})".format(l.start(), l.end() - 1))
        l = pattern.search(a,l.start() + 1)

else: print("(-1, -1)")
