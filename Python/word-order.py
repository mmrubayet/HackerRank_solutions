from collections import OrderedDict
words = OrderedDict()
for _ in range(int(input())):
    w = input()
    words.setdefault(w, 0)
    words[w] += 1
print(len(words))
print(*words.values())
