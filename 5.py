"""
Competitive Teams

第一行输入n,q  n表示开发者数量，分别为1至n。q表示queries的数量
接下来的每一行代表一次queries，有两种形式
第一个数字为1表示第一种形式，1后两个数字x，y 表示合并x，y所在两个团队
第一个数字为2表示第二种形式，2后一个数字c，c表示一个竞争常数，需返回满足|T1 - T2| >= c的情况总数
T1 T2分别为不同的团队的人数，即每两团队人数比较一次，获取满足式子的次数。
"""

# !/bin/python3

import os
import sys


# Complete the competitiveTeams function below.
def competitiveTeams(n, q):
    # 尝试提高速度，收集请求，重复请求直接调用结果。（不完善）
    requests = {}
    developers = init(n)
    group = []
    # 初始化组，每个人单独为一组，用序列表示组
    for i in developers:
        group.append([i])

    # queries
    for i in range(q):
        in_str = input()
        in_list = in_str.split()
        if in_str in requests:
            print(requests[in_str])
            continue
        requests = {}

        # 合并组请求
        if int(in_list[0]) == 1:
            x = int(in_list[1])
            y = int(in_list[2])
            x = get_group(x, group)
            y = get_group(y, group)
            z = x + y

            z = list(set(z))
            group.remove(x)
            if y in group: group.remove(y)
            group.append(z)
        # 竞争请求
        else:
            c = int(in_list[1])
            result = 0
            len_list = []
            for i in group:
                len_list.append(len(i))
            len_list.sort()
            for i in range(len(len_list), 0, -1):
                for j in range(i-1, 0, -1):
                    if len_list[i-1] - len_list[j-1] >= c:
                        result += j
                        break
            requests[in_str] = result
            print(result)


def init(n):
    developers = list(range(1, n + 1))
    return developers


def get_group(x, group):
    for i in group:
        if x in i:
            return i

    # Print the answer for each query of type 2. Take the query data from the standard input.


if __name__ == '__main__':
    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    competitiveTeams(n, q)
