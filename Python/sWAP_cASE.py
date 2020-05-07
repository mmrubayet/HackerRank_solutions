def swap_case(s):
    return ''.join([i.lower() if i.isupper() else i.upper() for i in s])

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#
# def swap_case(s):
#     a = ""
#     for i in s:
#         if i.isupper() == True:
#             a+=(i.lower())
#         else:
#             a+=(i.upper())
#     return a
