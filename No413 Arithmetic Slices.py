class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        count = 0
        num = 0
        for i in range(2, len(A)):
            if A[i]-A[i-1] == A[i-1] - A[i-2]:
                count += 1
                num += count
            else:
                count = 0
        return num
    