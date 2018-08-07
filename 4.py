"""
Balanced Sequence

https://www.hackerrank.com/contests/world-codesprint-13/challenges/balanced-sequence

一个序列不是一个平衡序列出现的点在于
1、从左向右数，第一次出现右括号数大于左括号数
2、从右向左数，第一次出现左括号数大于右括号数
只要出现上述一种情况则需要进行题目所给操作1次
每种情况只需一次操作即可改正，故result只有0,1,2三种
"""

# !/bin/python3

import os
import sys


# Complete the fewestOperationsToBalance function below.
def fewestOperationsToBalance(s):
    left, right = 0, 0
    for i in s:
        if i == '(':
            left += 1
        else:
            if left > 0:
                left -= 1
            else:
                right += 1

    if (left == 0 and right == 0):
        return 0
    elif (left == 0 or right == 0):
        return 1
    else:
        return 2
    # Return the minimum number of steps to make s balanced.


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = fewestOperationsToBalance(s)

    fptr.write(str(result) + '\n')

    fptr.close()
