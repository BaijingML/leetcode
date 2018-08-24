class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA, sumB, setB = sum(A), sum(B), set(B)
        temp = (sumB - sumA)/2
        for i in A:
            if temp + i in setB:
                return [i, temp+i]

if __name__ == '__main__':
    solu = Solution()
    print(solu.fairCandySwap([1,2,5], [2,4]))