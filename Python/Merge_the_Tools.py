def merge_the_tools(s, k):
    print(*[''.join(list(dict.fromkeys((list(s[i:(i+k)]))))) for i in range(0, len(s), k)], sep='\n')
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# def merge_the_tools(s, k):
#     for i in range(0, len(s), k):
#         print(''.join(list(dict.fromkeys((list(s[i:(i+k)]))))))
# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)
