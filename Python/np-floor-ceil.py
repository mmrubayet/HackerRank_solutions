import numpy as np
np.set_printoptions(legacy='1.13')
a = np.array(input().split(), float)
print(np.floor(a), np.ceil(a), np.rint(a), sep='\n')

# print(np.floor(a))
# print(np.ceil(a))
# print(np.rint(a))
