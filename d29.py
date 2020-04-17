t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    maxab = 0

    for a in range(n-1, 1, -1):
        for b in range(n, a, -1):
            ab = a&b
            if ab < k and ab > maxab:
                maxab = ab
            if maxab == k-1:
                break
        if maxab == k-1:
            break
    print(maxab)
