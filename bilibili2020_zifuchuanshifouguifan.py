#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/20 21:26
@File    : bilibili2020_zifuchuanshifouguifan
@Software: PyCharm
"""
if __name__ == "__main__":
    while True:
        try:
            s = input()
            result = "true"
            if not s:
                result = "false"
            elif len(s) == 1:
                result = "true"
            else:
                if ord(s[0]) >= ord("a"):
                    flag = "small"
                else:
                    flag = "Big"

                if flag == "small":
                    for i in s[1:]:
                        if ord(i) >= ord("a"):
                            continue
                        else:
                            result = "false"
                            break
                if flag == "Big":
                    if ord(s[1]) >= ord("a"):
                        flag = "small"
                        for i in s[1:]:
                            if ord(i) >= ord("a"):
                                continue
                            else:
                                result = "false"
                                break
                    else:
                        for i in s[1:]:
                            if ord(i) < ord("Z"):
                                continue
                            else:
                                result = "false"
                                break
            print(result)
        except:
            break