class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        return self.add(num)
    def add(self, n):
        num_str = str(n)
        if len(num_str) == 1:
            return n
        else:
            single_sum = 0
            for i in num_str:
                single_sum += int(i)
        return self.add(single_sum)

if __name__ == '__main__':
    solu = Solution()
    print(solu.addDigits(38))