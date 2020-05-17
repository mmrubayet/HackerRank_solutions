import numpy as np
n = int(input())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a.dot(b))
