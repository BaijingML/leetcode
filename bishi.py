# 笔试，求字符串的子串是否和另一个字符串相似，能够进行元素的一对一替换就是相似
# # 输入一个S所有字串的列表和T
# def jishu(S_list, T):
#     t_list = [] # T中每一个元素数量的列表
#     t = set(T) #    求集合
#
#     for i in t:
#         t_list.append(T.count(i))
#
#     nums = 0
#     for i in S_list:    # 遍历S的子串
#         if len(T) != len(i):
#             continue
#         else:
#             s = set(i)      # 求每一个子串的集合
#             if len(s) == len(t):    # 与T的集合不相等就不是
#                 flag = 1
#                 for j in s:     # 比较集合中每一个元素的数量是不是和T的集合中每一个元素的数量一致
#                     if i.count(j) in t_list:
#                         continue
#                     else:
#                         flag = 0
#                         break
#                 if flag == 1:
#                     nums += 1
#             else:
#                 continue
#     return nums

# def zichuan(S):
#     tem = []
#     for i in range(len(S)):
#         for j in range(i+1, len(S)+1):
#             tem.append(S[i:j])
#     return tem
# print(jishu(zichuan('ssd'), 'dss'))

#  快手笔试，求字符串中的字符个数拼接成新的字符串
# def zishu(s):
#     s_list = list(set(s))
#     s_list.sort()
#     nums = []
#     for i in s_list:
#         s.count(i)
#         nums.append(s.count(i))
#     s_str = ''
#     for i in range(len(s_list)):
#         s_str += s_list[i]
#         if nums[i] == 1:
#             continue
#         else:
#             s_str += str(nums[i])
#     print(s_str)
# s = input()
# zishu(s)

# 快手笔试，求一个序列的前M个最大子序列的和，各个子序列不能有交叠元素
# def max_nums(N, M, S_list):
#     max_nums = 0
#     for i in range(M):
#         one_sum = 0
#         temp_sum = 0
#         left = 0
#         right = -1
#         one_left = 0
#         for j in range(len(S_list)):
#             temp_sum += int(S_list[j])
#             if temp_sum > one_sum :
#                 one_left = left
#                 right = j
#                 one_sum = temp_sum
#             if temp_sum < 0:
#                 temp_sum = 0
#                 left = j+1
#         del S_list[one_left:right+1]
#         max_nums +=one_sum
#     return max_nums
# N, M=map(int,input().split())
# S_list = input().split()
# print(max_nums(int(N), int(M), S_list))

# 计算序列中出现频率最高的两个数的次数之和
# def fre_add(s_list):
#     s_set = set(s_list[1:])
#     frequence = []
#     for i in s_set:
#         frequence.append(s_list.count(i))
#     s_dict  = dict(zip(s_set, frequence))
#     s = sorted(s_dict.items(), key=lambda d: d[1], reverse=True)
#     return int(s[0][0])+int(s[1][0])

# def schedule(s_list):
#     s_pair = []
#     nums = 0
#     flag = [0]*len(s_pair)
#     for i in range(0, len(s_list[1:]), 2):
#         s_pair.append((float(s_list[1+i]), float(s_list[2+i])))
#     print(s_pair)
#     for i in range(len(s_pair)):
#         if i == len(s_pair) - 1:
#             return nums
#         for j in range(i+1, len(s_pair)):
#             if s_pair[i][1] > s_pair[j][0] and :
#                 flag[i+j+1] = 1
#                 nums += 1
#     return nums
# s_list = input().split()
# s_list = [10, 8 , 10, 8, 10, 8, 10, 8, 10, 12, 14.5]
# print(schedule(s_list))

# 腾讯数据挖掘笔试，计算字符串A的长度为k的子串在B中出现的次数之和，现在这个做法内存超限，怎么改进？
# 返回长度为k的子串
# def zichuan(S, k):
#     tem = []
#     for i in range(0, len(S)-k+1):
#         tem.append(S[i:i+k])
#     return set(tem)
#
# def zichuan_frequence(A, B, k):
#     nums = 0
#     A_list = zichuan(A, k)
#     for j in range(0, len(B) - k + 1):
#         if B[j:j+k] in A_list:
#             nums += 1
#     return nums
# k = int(input())
# A = input()
# B = input()
# print(zichuan_frequence(A, B, k))

# 腾讯数据挖掘笔试，计算X, Y, Z共可以生成多少个边长小于等于这三个值的三角形。

# def triangle_nums(X, Y, Z):
#     nums = 0
#     for i in range(1, X+1, 1):
#         for j in range(1, Y+1, 1):
#             for k in range(abs(i-j)+1, min(Z+1, i+j), 1):
#                 if i < j + k and j < i + k:
#                     print(i, j, k)
#                     nums += 1
#     return nums
# X, Y, Z = 2, 3, 3
# X, Y, Z = input().split()
# print(triangle_nums(int(X), int(Y), int(Z)))

# 中缀表达式转为后缀表达式，然后计算表达式的值

# expression = "3+(6*7-2)+2*3"
#
# def middle2behind(expresssion):
#     result = []             # 结果列表
#     stack = []              # 栈
#     for item in expression:
#         if item.isnumeric():      # 如果当前字符为数字那么直接放入结果列表
#             result.append(item)
#         else:                     # 如果当前字符为一切其他操作符
#             if len(stack) == 0:   # 如果栈空，直接入栈
#                 stack.append(item)
#             elif item in '*/(':   # 如果当前字符为*/（，直接入栈
#                 stack.append(item)
#             elif item == ')':     # 如果右括号则全部弹出（碰到左括号停止）
#                 t = stack.pop()
#                 while t != '(':
#                     result.append(t)
#                     t = stack.pop()
#             # 如果当前字符为加减且栈顶为乘除，则开始弹出
#             elif item in '+-' and stack[len(stack)-1] in '*/':
#                 if stack.count('(') == 0:           # 如果有左括号，弹到左括号为止
#                     while stack:
#                         result.append(stack.pop())
#                 else:                               # 如果没有左括号，弹出所有
#                     t = stack.pop()
#                     while t != '(':
#                         result.append(t)
#                         t = stack.pop()
#                     stack.append('(')
#                 stack.append(item)  # 弹出操作完成后将‘+-’入栈
#             else:
#                 stack.append(item)# 其余情况直接入栈（如当前字符为+，栈顶为+-）
#
#     # 表达式遍历完了，但是栈中还有操作符不满足弹出条件，把栈中的东西全部弹出
#     while stack:
#         result.append(stack.pop())
#     # 返回字符串
#     return "".join(result)
#
#
# print(middle2behind(expression))

# 招商银行笔试，有1对兔子，从出生后第7个月起每三个月都生一对小兔子，小兔子长到第7个月后每三个月又生一对兔子，问第N个月共有几对兔子

# def rabbit_sum(N):
#     if N < 10:
#         return 1
#     else:

# 百度笔试，括号匹配
# 判断是不是左括号，如果是在后面加右括号，否则在前面加左括号。
# def bracket_matching(s):
#     count = 0
#     pre = ''
#     for i in s:
#         if i == '[':
#             count += 1
#         else:
#             count -= 1
#         if count < 0:
#             count += 1
#             pre += '['
#     return pre+s+']'*count
#
# print(bracket_matching(']]][[[]]'))

# 快排的实现
S = [11,3,4,6,8,1,3,9,10,33,7,23]
# def partion(S, low, high):
#     pivot = S[low]
#     while low < high:
#         while low < high and S[high] >= pivot:
#             high -= 1
#         S[high], S[low] = S[low], S[high]
#         while low < high and S[low] <= pivot:
#             low += 1
#         S[high], S[low] = S[low], S[high]
#     return low
# def quick_sort(S, low, high):
#     if low < high:
#         pivot = partion(S, low, high)
#         quick_sort(S, low, pivot - 1)
#         quick_sort(S, pivot + 1, high)
#     return S

# def partion(S, low, high):
#     while low < high:
#         pivot = S[low]
#         while low < high and S[high] >= pivot:
#             high -= 1
#         S[low], S[high] = S[high], S[low]
#         while low < high and S[low] <= pivot:
#             low += 1
#         S[low], S[high] = S[high], S[low]
#     return low
# def quick_sort(S, low, high):
#     if low < high:
#         pivot = partion(S, low, high)
#         quick_sort(S, low, pivot - 1)
#         quick_sort(S, pivot + 1, high)
#     return S
# print(quick_sort(S, 0, len(S) - 1))

# def count_frequence(S):
#
#   res = dict()
#   for i in S:
#     if i in res:
#       res[i] += 1
#     else:
#       res[i] = 1
#     return res
# print(count_frequence('ed aa 3w3w'))

# import numpy as np
# import cv2
#
# im_path1 = 'D:/tu/front.jpg'
# im_path2 = 'D:/tu/behind.jpg'
# final_path = 'D:/tu/new.jpg'
# front = cv2.imread(im_path1)
# behind = cv2.imread(im_path2)
# print(front.shape, behind.shape)
# # emptyImage = np.zeros((3666 * 2, 2592), dtype=int)
# new_behind = cv2.resize(behind, (3666, 2592))
# new = np.concatenate((front, new_behind), axis=0)
# print(new.shape)
# cv2.imwrite(final_path, new)

# 360的题目，http://exercise.acmcoder.com/online/online_judge_ques?ques_id=3382&konwledgeId=42
# def judge(s):
#     flag = False
#     try:
#         first_index = s[0].index(s[1])
#     except:
#         return False
#     try:
#         print(s[0][first_index+len(s[1]):])
#         second_index = s[0][first_index+len(s[1]):].index(s[2]) + first_index+len(s[1])
#         print(second_index)
#     except:
#         return False
#     if first_index < second_index:
#         return True
# s = []
# while True:
#     s.append(input())
#     if len(s) == 3:
#         front_result = judge(s)
#         s[0] = s[0][::-1]
#         behind_result = judge(s)
#         if front_result and behind_result:
#             print('both')
#         elif front_result:
#             print('forward')
#         elif behind_result:
#             print('backward')
#         else:
#             print('invalid')
#         s = []

#　360的题目，http://exercise.acmcoder.com/online/online_judge_ques?ques_id=3383&konwledgeId=42
# def count(s):
#     num = [0] * 9
#     for i in range(len(s)):
#         if i == 4:
#             continue
#         if s[i] == 'X':
#             num[i] = i + 1
#     print(sum(num))
#     if sum(num) % 10 == 0:
#         return True
#     else:
#         return False
# s = []
# while True:
#     s.append(input())
#     if len(s) == 3:
#         new_s = s[0] + s[1] + s[2]
#         if count(new_s):
#             print('YES')
#         else:
#             print('NO')
#         s = []


# def arrange(n, m, s):
#     if m > n:
#         return None
#     x = 2*m - n
#     s.sort()
#     length = len(s)
#     s = s[:length-x]
#     print(s, len(s))
#     max_num = 0
#     for i in range(int(len(s)/2)):
#         print(s[len(s)-i-1])
#         max_num = max(s[i]+s[len(s)-i-1], max_num)
#     return max_num
# s = []
# while True:
#     s.append(input())
#     if len(s) == 2:
#         print(s)
#         m = int(s[0][0])
#         n = int(s[0][2])
#         s = s[1].split(' ')
#         new_s = []
#         for i in s:
#             new_s.append(int(i))
#         print(arrange(m, n, new_s))
#         s = []

w = 10
b = 5
def countandsum(w, b):
    result = [[0 for i in range(w)] for j in range(b)]
    num_sum = w + b
    count = 1
    left_w = w
    for i in range(w):
        if count > left_w:
            result[i][0] = 1
            count += 1
            left_w -= count
    count = 1
    left_b = b
    for j in range(b):
        if count > left_b:
            result[0][j] = 1
            count += 1
            left_b -= count
    for i in range(1, w):
        for j in range(1, b):
            if i+j+2 > w and i+j+2 > b:
                continue
            elif i+j+2 > w:
    return count, all_method

w, b = input().split(' ')
count, all_method = countandsum(int(w), int(b))
print(count, all_method)



















