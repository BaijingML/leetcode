class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        prime_num = 0
        for i in range(L, R+1):
            num = bin(i)[2:].count('1')
            if num in prime:
                prime_num += 1
        return prime_num

print(Solution.countPrimeSetBits(Solution, 842, 888))
