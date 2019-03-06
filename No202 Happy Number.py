class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 1:
            return False
        num_set = set()
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in num_set:
                return False
            else:
                num_set.add(n)
            print(n)
        return True
if __name__ == '__main__':
    Solu = Solution()
    print(Solu.isHappy(7))