#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/8 18:55
@File    : bishi1
@Software: PyCharm
"""
# if __name__ == "__main__":
#     N, K = input().split(" ")
#     N, K = int(N), int(K)
#     nums = str(input())
#     print(N, K, nums)
#     new = [0] * N
#     new[0] = int(nums[0])
#     m = len(nums)
#     new[N - 1] = int(nums[m-1])
#     for i in range(1, K):
#         new[i] = int(nums[i]) ^ int(nums[i-1])
#     for j in range(K+1, N-1):
#         temp = new[j-K]
#         for i in range(j-K+1, j):
#             temp = new[i] ^ temp
#         new[j] = temp ^ int(nums[j])
#     print(new)
# 求数组的最大子序列和
# if __name__ == "__main__":
#     N = int(input())
#     nums = []
#     for i in range(N):
#         nums.append(int(input()))
#     dp = [-float('inf')] * N
#     dp[0] = nums[0]
#     for i in range(1, N):
#         dp[i] = max(nums[i], dp[i-1]+nums[i])
#     print(max(dp))


# from heapq import *
# if __name__ == "__main__":
#
#     K, N = input().split(" ")
#     K, N = int(K), int(N)
#     nums = []
#     temp_min = []
#     for i in range(N):
#         nums.append([int(i) for i in input().split(" ")])
#     heappush(temp_min, (nums[0][0], 0, 0))
#     while K > 0:
#         ret, i, j = heappop(temp_min)
#         if i == 0 and j + 1 < N:
#             heappush(temp_min, (nums[i][j+1], i, j+1))
#         if i+1 < N:
#             heappush(temp_min, (nums[i+1][j], i+1, j))
#         K -= 1
#     print(ret)
# if __name__ == "__main__":
#     N = int(input())
#     nums = input().split(" ")
#     for i in range(N):
#         nums[i] = int(nums[i])
#     nums.sort()
#     min_sum = float("inf")
#     max_sum = -float("inf")
#     for i in range(int(N/2)):
#         if nums[i] + nums[N-i-1] > max_sum:
#             max_sum = nums[i] + nums[N-i-1]
#         if nums[i] + nums[N-i-1] < min_sum:
#             min_sum = nums[i] + nums[N-i-1]
#     print(max_sum - min_sum)

# def expand(m, n, x, y, K, result):
#     dp[x][y] = 1
#     if K > 0:
#         if 0 < x < m - 1 and 0 < y < n - 1:
#             if dp[x - 1][y] == 0:
#                 result += expand(m, n, x - 1, y, K - 1, result)
#             if dp[x][y - 1] == 0:
#                 result += expand(m, n, x, y - 1, K - 1, result)
#             if dp[x + 1][y] == 0:
#                 result += expand(m, n, x + 1, y, K - 1, result)
#             if dp[x][y + 1] == 0:
#                 result += expand(m, n, x, y + 1, K - 1, result)
#             return result
#         elif x == 0 or y == 0 or x == m - 1 or y == n - 1:
#             result += 1
#             print(111111111)
#             return result
#         else:
#             return 0
#     else:
#         return 0
# if __name__ == "__main__":
#     m, n, x, y, K = int(input()), int(input()), int(input()), int(input()), int(input())
#     dp = [[0 for i in range(n)] for j in range(m)]
#     dp[x][y] = 1
#     result = 0
#     if K < 1:
#         print(0)
#     else:
#         result += expand(m, n, x - 1, y, K - 1, result)
#         result += expand(m, n, x, y - 1, K - 1, result)
#         result += expand(m, n, x + 1, y, K - 1, result)
#         result += expand(m, n, x, y + 1, K - 1, result)
#         print(result)
#         print(dp)

# 计算一个字符串内有几个回文子串
# def judge(s):
#     m = len(s)
#     for i in range(int(m/2)):
#         if s[i] == s[m-1-i]:
#             continue
#         else:
#             return False
#     return True
# if __name__ == "__main__":
#     s = input()
#     n = len(s)
#     count = n
#     if not s:
#         print(0)
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if judge(s[i:j+1]):
#                 count += 1
#     print(count)
# 交换苹果的次数，使得每个人的数量相同
# if __name__ == "__main__":
#     n = int(input())
#     nums = input().split(" ")
#     for i in range(n):
#         nums[i] = int(nums[i])
#     average = sum(nums) // n
#     if sum(nums) % n != 0:
#         print(-1)
#     else:
#         count = 0
#         for i in nums:
#             if i < average:
#                 temp = average - i
#                 if temp % 2 != 0:
#                     print(-1)
#                     break
#                 count += int(temp / 2)
#         print(count)

# if __name__ == "__main__":
#     nums = input()
#     n = len(nums)
#     nums = nums[1:(n-1)]
#     nums = list(map(int, nums.split(",")))
#     d = {}
#     for i in nums:
#         if i in d.keys():
#             d[i] += 1
#         else:
#             d[i] = 1
#     max_value = -float("inf")
#     key = 0
#     for i in d.keys():
#         if d[i] > max_value:
#             max_value = d[i]
#             key = i
#     print(key)

if __name__ == "__main__":
    N, M = input().split(" ")
    N, M = int(N), int(M)
    s1 = list(map(int, input().split(" ")))
    s2 = list(map(int, input().split(" ")))
    temp = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][j] = (s1[i] + s2[j]) % M
    result = ['' for i in range(N)]
    index = []
    for i in range(N):
        for j in range(N):
            t = max(temp[i])
            index = temp[i].index(t)
            for j in range(N):
                temp[j][index] = -1
            result[i] += ' ' + str(t)
    r = max(result)
    print(r)
