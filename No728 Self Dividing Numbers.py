def selfDividingNumbers(left, right):
    m = []
    for i in range(left,right+1):
        if '0' in str(i):
            pass
        else:
            self_div = True
            for j in str(i):
                if i % int(j) != 0:
                    self_div = False
                    break
            if self_div:
                m.append(i)
    return m
left = 1
right = 22
print(selfDividingNumbers(left, right))


