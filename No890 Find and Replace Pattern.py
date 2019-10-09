#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/10/8 19:18
@File    : No890 Find and Replace Pattern
@Software: PyCharm
"""
class Solution:
    def findAndReplacePattern(self, words, pattern):
        result = []
        n = len(pattern)
        for i in words:
            if len(i) != n:
                continue
            else:
                d = {}
                flag = True
                for j in range(n):
                    if pattern[j] in d.keys():
                        if i[j] == d[pattern[j]]:
                            continue
                        else:
                            flag = False
                            break
                    else:
                        if i[j] in d.values():
                            flag = False
                        else:
                            d[pattern[j]] = i[j]
                # print(d)
                if flag: result.append(i)
        return result
if __name__ == '__main__':
    solu = Solution()
    print(solu.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))