#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/10/3 23:07
@File    : No1047 Remove All Adjacent Duplicates In String
@Software: PyCharm
"""
class Solution:
    def removeDuplicates(self, S: str) -> str:
        flag = True
        s_list = list(S)
        while flag:
            flag = False
            to_deleted = False
            for i in range(len(s_list)-1, 0, -1):
                if to_deleted:
                    s_list.remove(s_list[i])
                    continue
                if s_list[i] == s_list[i-1]:
                    s_list.remove(s_list[i])
                    to_deleted = True
                    flag = True
            print(s_list)
        return "".join(s_list)


if __name__ == '__main__':
    solu = Solution()
    print(solu.removeDuplicates("abbaca"))