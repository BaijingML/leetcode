#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/6 19:39
@File    : xiaomi2020_yichuKgezifu
@Software: PyCharm
"""

# def getnums(num, k):
#     while k > 0:
#         k -= 1
#         i = 0
#         while i < len(num) - 1:
#             if num[i] > num[i + 1]:
#                 break
#             i += 1
#         num = num[:i] + num[i + 1:]
#
#     if len(num) == 0:
#         return "0"
#     else:
#         return str(int(num))
# if __name__ == "__main__":
#     str1, K = input().split(",")
#     K = int(K)
#     print(getnums(str1, K))

def getprofit(prices):
    profit = 0
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            profit += prices[i+1] - prices[i]
    return profit
if __name__ == "__main__":
    nums = list(map(int, input()[1:-1].split(",")))
    print(getprofit(nums))