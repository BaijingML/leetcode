class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        plus = 0
        digits[-1] = digits[-1] + 1
        if digits[-1] > 9:
            plus = 1
            digits[-1] = 0
            if len(digits) == 1:
                return [plus, digits[-1]]
        for i in range(len(digits)-2, 0, -1):
            if digits[i] + plus > 9:
                digits[i] = 0
                plus = 1
            else:
                digits[i] = digits[i] + plus
                plus = 0
        if digits[0] + plus > 9:
            digits[0] = 0
            digits.insert(0, 1)
        else:
            digits[0] = digits[0] + plus
        return digits
if __name__ == '__main__':
    solu = Solution()
    print(solu.plusOne([9, 9]))