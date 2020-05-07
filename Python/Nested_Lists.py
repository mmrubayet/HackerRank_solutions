marksheet = [[input(), float(input())] for _ in range(int(input()))]
sh = sorted(list(set([marks for name, marks in marksheet])))
print('\n'.join([a for a,b in sorted(marksheet) if b == sh]))
