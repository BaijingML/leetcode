#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/21 19:07
@File    : huawei2020
@Software: PyCharm
"""
if __name__ == "__main__":
    nums = input().split(" ")
    if nums:
        n = eval("0x" + nums[0])
        result = []
        for i in range(1, n):
            if nums[i] == "A":
                result.append("12")
                result.append("34")
            elif nums[i] == "B":
                result.append("AB")
                result.append("CD")
            else:
                result.append(nums[i])
        m = len(result)
        result.insert(0, hex(m+1)[2:])

        print(" ".join(result))
    else:
        print("")

# if __name__ == "__main__":
#     import math
#     low, high = input().split(" ")
#     low, high = int(low), int(high)
#     temp = []
#     for i in range(low, high):
#         for j in range(2, int(math.sqrt(i) +1)):
#             if i % j == 0:
#                 break
#         else:
#             temp.append(i)
#     sum1, sum2 = 0, 0
#     if temp[0] > 9:
#         for i in range(len(temp)):
#             # sum1 += int(str(temp[i])[-2])
#             # sum2 += int(str(temp[i])[-1])
#             sum1 += temp[i] % 10
#             sum2 += int(temp[i] / 10) % 10
#         print(min(sum1, sum2))
#     else:
#         for i in range(len(temp)):
#             sum1 += int(str(temp[i])[-1])
#         print(sum1)


# if __name__ == "__main__":
#     start = input()
#     N = int(input())
#     W = []
#     name = set()
#     name.add(start)
#     for i in range(N):
#         temp = input().split(",")
#         W.append(temp)
#     starts = []
#     count = 0
#     for line in W:
#         if start in line:
#             for j in line:
#                 if j not in name:
#                     starts.append(j)
#                     name.add(j)
#     while starts:
#         s = starts.pop(0)
#         for line in W:
#             if s in line:
#                 for j in line:
#                     if j not in name:
#                         name.add(j)
#                         starts.append(j)
#     print(len(name))






