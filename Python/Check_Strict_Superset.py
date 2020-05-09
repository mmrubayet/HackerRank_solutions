s = set(input().split())
print(all(s > set(input().split()) for _ in range(int(input()))))
