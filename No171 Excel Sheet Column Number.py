class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 大写字母的ASCII码范围是65-91，小写字母是97-123
        num = 0
        alpha_num_dict = {chr(j):j-64 for j in range(65,91)}
        n = len(s)
        if n == 1:
            return alpha_num_dict[s]
        for i in range(n):
            num += alpha_num_dict[s[i]] * 26**(n-1-i)
        return num


if __name__ == '__main__':
    solu = Solution()
    print(solu.titleToNumber('ZY'))