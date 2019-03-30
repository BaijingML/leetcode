class Solution:
    def sortedSquares(self, A):
        if not A:
            return []
        start = 0
        end = len(A) - 1
        result = [0] * len(A)
        while start <= end:
            print(start, end)
            a = A[start] ** 2
            b = A[end] ** 2
            if a <= b:
                result[end-start] = b
                end -= 1

            else:
                result[end-start] = a
                start += 1
        return result

if __name__ == '__main__':
    Solu = Solution()
    print(Solu.sortedSquares([-4,-1,0,3,10]))