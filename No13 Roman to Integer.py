def romanToInt( s):
    """
    :type s: str
    :rtype: int
    """
    to_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = pre_num = 0
    ss = s[::-1]
    for i in range(len(ss)):
    #for i in range(len(s), -1, -1):
        print(i)
        cur_num = to_dict[ss[i]]
        if cur_num < pre_num:
            num -= cur_num
        else:
            num += cur_num
        pre_num = cur_num
    return num
print(romanToInt("MDCXCV"))