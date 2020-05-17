import numpy as np
p = np.array(input().split(), dtype=float)
x = int(input())
print(np.polyval(p,x))
