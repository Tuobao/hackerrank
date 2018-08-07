#!/bin/python3
"""
Group Formation

https://www.hackerrank.com/contests/world-codesprint-13/challenges/group-formation

满分30 得分17.76
未通过四个测试单元，原因是超时
代码太臃肿，需改善代码。提高计算速度
"""

import os
import sys

# Complete the membersInTheLargestGroups function below.
def membersInTheLargestGroups(n, m, a, b, f, s, t):

    # 存学生字典
    for i in range(n):
        k, v = input().split()
        students[k] = v


    for i in range(m):
        x, y = input().split()
        x = in_group(x)
        y = in_group(y)


        # str与str  str与list  list与str  list与list四种情况的建组
        if type(x)==str and type(y)==str:
            z = [x, y]
        elif type(x)==str:
            z = y.copy()
            z.append(x)
        elif type(y)==str:
            z = x.copy()
            z.append(y)
        else:
            if x == y:
                continue
            z = x + y

        # 去重
        z = list(set(z))

        # 验证列表是否符合要求
        if check(z):
            if x in result: result.remove(x)
            if y in result: result.remove(y)
            result.append(z)

    # 除去不满最小人数的组
    for i in result[::-1]:
        if len(i) < a:
            result.remove(i)

    # 获取有效组的最大长度
    max_len = 0
    for i in range(len(result)):
        if len(result[i]) > max_len:
            max_len = len(result[i])


    if not result:
        print('no groups')
    else:
        # 考虑到出现人数为max_len有多组的情况，合并最后结果
        result_new = []
        for i in result:
            if len(i) != max_len:
                continue
            for j in i:
                # 获取到所有人数为max_len的组，并合并
                result_new.append(j)
        result_new.sort()
        for i in result_new:
            print(i)



    # Print the names of the students in all largest groups or determine if there are no valid groups.

# 判断该生是否已经有组了，有则返回组，没有则返回本身
def in_group(x):
    for i in result:
        if x in i:
            return i
    return x

# 检查组是否满足规则
def check(z):
    if len(z) > b:
        return False
    grade = {'q': [], 'w': [], 'e':[]}
    for i in z:
        if students[i] == '1': grade['q'].append(i)
        if students[i] == '2': grade['w'].append(i)
        if students[i] == '3': grade['e'].append(i)
    if len(grade['q'])>f or len(grade['w'])>s or len(grade['e'])>t:
        return False
    return True

if __name__ == '__main__':
    nmabfst = input().split()

    n = int(nmabfst[0])

    m = int(nmabfst[1])

    a = int(nmabfst[2])

    b = int(nmabfst[3])

    f = int(nmabfst[4])

    s = int(nmabfst[5])

    t = int(nmabfst[6])

    students = {}
    result = []

    membersInTheLargestGroups(n, m, a, b, f, s, t)
