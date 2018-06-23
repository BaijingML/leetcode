
def numJewelsInStones(J, S):
    n = 0
    for i in S:
        if i in J:
            n += 1
    return n
J = 'aA'
S = 'aAAbbbb'
print(numJewelsInStones(J, S))
