import re
for _ in range(int(input())):
    n, e = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', e)
    if m:
        print(n, e)


# import email.utils
# import re
# for _ in range(int(input())):
#     n, m = input().split('<')
#     n = n.strip()
#     e, m = m.split('>')
#     m = re.match(r'[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}', e)
#     if m:
#         print(email.utils.formataddr((n, e)))
