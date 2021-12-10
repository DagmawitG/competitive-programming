#!/bin/python3

import math
import os
import random
import re
import sys


# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    swaps = 0
    for i in range(0,n):
        for j in range(0,n-1):
            if(a[j] > a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]
                swaps+=1
    print("Array is sorted in "+str(swaps)+" swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))
    return

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
