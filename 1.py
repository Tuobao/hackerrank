"""
Find The Absent Students

有学号为1至n的学生，现给出一个长度为n的序列，序列内只出现1至n中的数
获取1至n中没有在序列中出现的数
"""


import os
import sys

# Complete the findTheAbsentStudents function below.
def findTheAbsentStudents(n, a):
    b = []
    for i in range(1, n+1):
        if i not in a:
            b.append(i)
    return b
    # Return the list of student IDs of the missing students in increasing order.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = findTheAbsentStudents(n, a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
