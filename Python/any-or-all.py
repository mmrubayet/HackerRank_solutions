n, ar = int(input()), input().split()
print(all([int(i)>0 for i in ar]) and any([j == j[::-1] for j in ar]))
