#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/23 18:16
@File    : beike2020_ceshi
@Software: PyCharm
"""
"""平方根的和"""
# if __name__ == "__main__":
#     import math
#     while True:
#         try:
#             N, M = list(map(int, input().split(" ")))
#             if N > 0:
#                 s = N
#                 for i in range(M-1):
#                     N = math.sqrt(N)
#                     s += N
#                 print('%.2f' % s)
#             else:
#                 print(0)
#         except:
#             break

"""水仙花数"""
# if __name__ == "__main__":
#     while True:
#         try:
#             m, n = list(map(int, input().split(" ")))
#             result = []
#             for i in range(m, n+1):
#                 t = (i % 10) ** 3 + (int(i / 10) % 10) ** 3 + int(i / 100) ** 3
#                 if i == t:
#                     result.append(str(i))
#                 else:
#                     continue
#             if result:
#                 print(" ".join(result))
#             else:
#                 print("no")
#         except:
#             break