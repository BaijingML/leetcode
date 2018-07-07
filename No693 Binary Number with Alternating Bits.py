def hasAlternatingBits(n):
    # 右移一位，然后按位异或
    return '0' not in bin(n ^ n >> 1)[2:]
