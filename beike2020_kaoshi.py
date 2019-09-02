#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/23 19:28
@File    : beike2020_kaoshi
@Software: PyCharm
"""
def cal(n, s, nums):
    if sum(nums) <= s:
        return n
    else:
        count = 0
        for i in nums:
            if s - i >= 0:
                count += 1
                s = s - i
            else:
                break
        return count

if __name__ == "__main__":
    while True:
        n, s = input().split(' ')
        n, s = int(n), int(s)
        nums = input().split(" ")
        for i in range(n):
                nums[i] = int(nums[i])
        nums.sort()
        print(cal(n, s, nums))


def campare(s, n):
    t = ""
    if s[0] == "x":
        t += "A"
    if s[1] == "x":
        t += "B"
    if s[2] == "x":
        t += "C"
    if s[3] == "x":
        t += "D"
    if t == n:
        return 5
    if not t:
        return 0
    for j in t:
        if j in n:
            continue
        else:
            return 0
    return 3


if __name__ == "__main__":
    while True:
        N = int(input())
        temp = []
        score = 0
        for i in range(N):
            temp = (input().split(" "))
            score += campare(temp[0], temp[1])
        print(score)

if __name__ == "__main__":
    N, T = list(map(int, input().split(" ")))
    count = 0
    for i in range(N):
        n, t = list(map(int, input().split(" ")))
        m = int(T / t)
        if m >= 1:
            if m <= n:
                T -= m * t
                count += m
            else:
                T -= n * t
                count += n
        if T < 0:
            break
    print(count)


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split(" ")))
    s = sum(nums)
    temp = [[0 for j in range(int(s / 2) + 1)] for i in range(N+1)]
    count = 0
    for i in range(1, N+1):
        for j in range(1, int(s / 2) + 1):
            if nums[i-1] > j:
                temp[i][j] = temp[i-1][j]
            else:
                temp[i][j] = temp[i-1][j-nums[i-1]] + nums[i-1]
    n = int(s/2)
    for i in range(N, 0, -1):
        if temp[i][n] == temp[i-1][n]:
            continue
        else:
            n = n- nums[i-1]
            count += 1
    print(s- 2*temp[N][int(s / 2)], abs(N - 2 * count))


