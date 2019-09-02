#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/24 13:57
@File    : tw2020_test
@Software: PyCharm
"""
def call(N, M, info):
    for i in range(N):
        for j in range(M):
            if N % 3 == 2 and N - i == 2:
                result[i][j] = info[int(i / 3) * M + j][1]
            elif N % 3 == 2 and N - i == 1:
                result[i][j] = info[int(i / 3) * M + j][0]

                if 0 <= i % 6 <= 2: # 确定是向右还是向左
                    if i % 3 == 0: # 在上方
                        result[i][j] = info[int(i / 3) * M + j][1]
                    if i % 3 == 1:
                        result[i][j] = info[int(i / 3) * M + j][0]
                    if i % 3 == 2:
                        result[i][j] = info[int(i / 3) * M + j][3]
                else:
                    if i % 3 == 0:
                        result[i][j] = info[int(i / 3) * M + M - j][1]
                    if i % 3 == 1:
                        result[i][j] = info[int(i / 3) * M + M - j][0]
                    if i % 3 == 2:
                        result[i][j] = info[int(i / 3) * M + M - j][3]
    return result
if __name__ == "__main__":
    N, M = list(map(int, input().split(" ")))
    # 建立空的结果矩阵
    result = [["" for _ in range(M)] for _ in range(N)]
    # 计算总的拍摄次数
    m = (int((N-1) / 3) + 1) * M
    info = []
    for i in range(m):
        info.append(input())
    print(call(N, M, info))





