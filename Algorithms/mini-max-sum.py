#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr = sorted(arr)
    print(sum(arr[:-1]), sum(arr[1:]))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

# arr = sorted(arr)
# ar = 0
# for i in range(0, len(arr)-1):
#     ar += arr[i]
# print(ar, end=' ')
# ar = 0
# for i in range(1, len(arr)):
#     ar += arr[i]
# print(ar)
