import math
n = int(input())
ar = str(input()).split(" ")
def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
el = unique(ar)
cnt = []
pr = 0
for i in range(len(el)):
    cnt.append(ar.count(el[i]))
    pr += math.floor(cnt[i] / 2)
print(pr)

'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    def unique(list1):
        unique_list = []
        for x in list1:
            if x not in unique_list:
                unique_list.append(x)
        return unique_list


    el = unique(ar)
    cnt = []
    pr = 0
    for i in range(len(el)):
        cnt.append(ar.count(el[i]))
        p = math.floor(cnt[i] / 2)
        pr += p

    return pr



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
'''
