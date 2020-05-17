import numpy as np
a, b = (np.array(input().split(), dtype=int) for _ in range(2))
print(np.inner(a,b), np.outer(a,b), sep='\n')
