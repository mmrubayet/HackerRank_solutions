import numpy as np
n, m, p = map(int, input().split())
arn = np.array([input().strip().split() for _ in range(n)], int)
arm = np.array([input().strip().split() for _ in range(m)], int)
print(np.concatenate((arn, arm)))
