#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/15 16:29
@File    : No841 Keys and Rooms
@Software: PyCharm
"""


class Solution:

    def canVisitAllRooms(self, rooms):
        temp = [0 for i in range(len(rooms))]
        self.dsf(0, temp, rooms)
        if sum(temp) == len(rooms):
            return True
        return False
    def dsf(self, start, temp, rooms):
        if temp[start] == 1:
            return
        temp[start] = 1
        for i in rooms[start]:
            self.dsf(i, temp, rooms)
if __name__ == '__main__':
    solu = Solution()
    print(solu.canVisitAllRooms([[1],[2],[3],[]]))