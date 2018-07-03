def findComplement(num):
    a = ''.join(str(1-int(i)) for i in bin(num)[2:])
    return int(a, 2)

print(findComplement(5))