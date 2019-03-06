class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if numRows == 0:
            return result
        if numRows == 1:
            return [[1]]
        if numRows > 1:
            result.append([1])
            for i in range(1, numRows):
                temp = [1] * (i+1)
                for j in range(1, i):
                    temp[j] = result[i-1][j-1] + result[i-1][j]
                result.append(temp)
        return result
if __name__ == '__main__':
    solu = Solution()
    print(solu.generate(5))