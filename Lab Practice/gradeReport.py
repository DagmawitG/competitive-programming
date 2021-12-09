#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    
    for i in range(0,len(grades)):
        if (grades[i]>=38):
            rem = (grades[i]+5) % 5
            
            num = grades[i] + 5 - rem
            if(num > grades[i]):
                if ((num - grades[i]) < 3):
                    grades[i] = num
                else:
                    grades[i] = grades[i]
        else:
            grades[i] = grades[i]
        
    return grades
                    
    
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
