t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    maximum = 0

    for a in range(n-1, 1, -1):
        for b in range(n, a, -1):
            ab = a&b
            if k > ab > maximum:
                maximum = ab
            if maximum == k-1:
                break
        if maximum == k-1:
            break
    print(maximum)
