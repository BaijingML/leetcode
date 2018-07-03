def hammingDistance(x, y):
    a = bin(x ^ y)
    return a.count('1')
x = 1
y = 4
print(hammingDistance(x, y))