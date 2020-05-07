n, m = map(int, input().split())
sp = ' '
mp = '_|_'
pattern = [(mp*(2*i + 1)).center(m, sp) for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, sp)] + pattern[::-1]))
# pt = ''
# p ='.|.'
# w = 'WELCOME'
# for i in range(1, n, 2):
#     pl = p*i
#     s = int((m-len(pl))/2)
#     pt += (('-'*s)+pl+('-'*s))
# print(pt)
# s = int((m-len(w))/2)
# print(('-'*s)+w+('-'*s))
#
# for i in range(n-2, 0, -2):
#     pl = p*i
#     s = int((m-len(pl))/2)
#     print(('-'*s)+pl+('-'*s))
