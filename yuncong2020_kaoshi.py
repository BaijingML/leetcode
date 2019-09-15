#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/8 18:57
@File    : oppo2020_kaoshi
@Software: PyCharm
"""
# if __name__ == '__main__':
#     str1 = input()
#     str2 = input()
#     m, n = len(str1), len(str2)
#     temp = [[0 for i in range(m+1)] for j in range(n+1)]
#     for i in range(n):
#         temp[0][i] = 1
#     for i in range(1, n):
#         for j in range(m):
#             if str2[i] == str1[j]:
#                 temp[i][j] = temp[i][j-1] + temp[i-1][j-1]
#             else:
#                 temp[i][j] = temp[i][j-1]
#     print(temp[n][m])

# if __name__ == '__main__':
#     str1 = input()
#     str2 = input()
#     m, n = len(str1), len(str2)
#     count = 0
#     for i in range(m):
#         if str1[i] == str2[0]:
#             if str1[i:i+n] == str2:
#                 count+=1
#     print(count)

# if __name__ == '__main__':
#     n, k = list(map(int, input().split(" ")))
#     temp = [[0 for i in range(k+1)] for j in range(n+1)]
#     temp[0][0] = 1
#     for i in range(1, n+1):
#         for j in range(1, k+1):
#             if i>= j:
#                 temp[i][j] = temp[i-j][j] + temp[i-1][j-1]
#     print(temp[n][k])

class struct():
    def __init__(self):
        self.nums = []

    def insert(self, n):
        self.nums.append(n)
        self.nums.sort()

    def delete(self, n):
        self.nums.remove(n)

    def query(self, n):
        self.nums.sort()
        index = self.nums.index(n)
        return index
    def query_index(self, n):

        return self.nums[n-1]
    def find_max(self, n):
        for i in range(len(self.nums)):
            if self.nums[i] > n:
                return self.nums[i]
    def find_min(self, n):
        for i in range(len(self.nums)-1, -1, -1):
            if self.nums[i] < n:
                return self.nums[i]
if __name__ == '__main__':
    solu = struct()
    N = int(input())
    for i in range(N):
        t,v = list(map(int, input().split(" ")))
        if t == 1:
            solu.insert(v)
        elif t == 2:
            solu.delete(v)
        elif t == 3:
            print(solu.query(v))
        elif t == 4:
            print(solu.query_index(v))
        elif t == 5:
            print(solu.find_min(v))
        else:
            print(solu.find_max(v))

