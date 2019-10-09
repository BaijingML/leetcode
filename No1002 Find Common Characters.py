#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/10/9 19:56
@File    : No1002 Find Common Characters
@Software: PyCharm
"""
class Solution:
    # def find(self, a, b):
    #     new = {}
    #     for i in a.keys():
    #         if i not in b.keys():
    #             continue
    #         else:
    #             new[i] = min(a[i], b[i])
    #     return new
    # def commonChars(self, A):
    #     d = {}
    #     for i in A[0]:
    #         if i in d.keys():
    #             d[i] += 1
    #         else:
    #             d[i] = 1
    #     for i in range(1, len(A)):
    #         temp = {}
    #         for j in A[i]:
    #             if j not in temp.keys():
    #                 temp[j] = 1
    #             else:
    #                 temp[j] += 1
    #         d = self.find(temp, d)
    #     result = []
    #     for i in d.keys():
    #         for j in range(d[i]):
    #             result.append(i)
    #     return result
    def commonChars(self, A):
        temp = list(A[0])
        for i in A[1:]:
            check = []
            for j in i:
                if j in temp:
                    check.append(j)
                    temp.remove(j)
            temp = check
        return temp

if __name__ == '__main__':
    solu = Solution()
    print(solu.commonChars(["cool","lock","cook"]))