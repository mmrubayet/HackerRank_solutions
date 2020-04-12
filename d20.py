def swap(a, x, y):
    tmp = a[x]
    a[x] = a[y]
    a[y] = tmp

def bubblesort(a):
    n = len(a)
    swapCount = 0
    for i in range(0, n):
        for j in range(0, n - 1):
            if a[j] > a[j + 1]:
                swap(a, j, j + 1)
                swapCount += 1

        if swapCount == 0:
            break
            
    return (a[0], a[n - 1], swapCount)

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

first, last, swaps = bubblesort(a)
print("Array is sorted in", swaps, "swaps.")
print("First Element:", first)
print("Last Element:", last)
