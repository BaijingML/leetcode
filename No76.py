#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/20 21:31
@File    : No76
@Software: PyCharm
"""
if __name__ == "__main__":
    import collections
    while True:
            try:
                s = input()
                t = input()
                temp = collections.defaultdict(int)
                for i in t:
                    temp[i] += 1
                left = 0
                right = 0
                count = len(temp)
                m = 2 * len(s)
                result = ""
                while right < len(s):
                    t = s[right]
                    if t in temp:
                        temp[t] -= 1
                        if temp[t] == 0:
                            count -= 1
                    right += 1
                    while count == 0:
                        if right - left < m:
                            m = right - left
                            result = s[left:right]
                        c  = s[left]
                        if c in temp:
                            temp[c] += 1
                            if temp[c] > 0:
                                count += 1
                        left += 1
                if result:
                    print(result)
                else:
                    print("#")