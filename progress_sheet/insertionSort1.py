#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    
    i = 0
    j = 1
    while i < len(arr)-1 or j < len(arr)-1:
        if arr[j] < arr[i]:
            temp = arr[j]
            arr[j] = arr[i]
            print(*arr)
            temp, arr[i]=arr[i], temp
            if i-1 < 0:
                i += 1
                j += 1
                continue
            else:
                i -= 1
                j -= 1
        else:
            i += 1
            j += 1
    print(*arr)
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
