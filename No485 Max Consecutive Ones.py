class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = 0
        ans = 0
        for i in nums:
            if i == 1:
                flag += 1
                ans = max(ans, flag)
            else:
                flag = 0
        return ans

        # 另一种写法
        # nums_str_list = ''.join(str(num) for num in nums).split('0')
        # return max(len(i) for i in nums_str_list)


if __name__ == '__main__':
    solu = Solution()
    print(solu.findMaxConsecutiveOnes([1,1,0,1,1,1]))