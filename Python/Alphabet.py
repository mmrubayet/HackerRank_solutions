import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    pattern = []
    width = 4*size-3
    for i in range(n):
        s = "-".join(alpha[i:n])
        pattern.append((s[::-1]+s[1:]).center(width, "-"))
    print('\n'.join(pattern[:0:-1]+pattern))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)



# import string
# alpha = string.ascii_lowercase
#
# n = int(input())
# pattern = []
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     pattern.append((s[::-1]+s[1:]).center(4*n-3, "-"))
# print('\n'.join(pattern[:0:-1]+pattern))
