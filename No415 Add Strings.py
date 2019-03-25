class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        str_sum, m, n = 0, len(num1) - 1, len(num2) - 1
        res = ''
        while m >= 0 or n >= 0 or str_sum > 0:
            if m >= 0:
                str_sum += ord(num1[m]) - ord('0')
                print(str_sum)
                m -= 1
            if n >= 0:
                str_sum += ord(num2[n]) - ord('0')
                print(str_sum)
                n -= 1
            print(str_sum % 10)
            res = str(str_sum % 10) + res
            str_sum  = int(str_sum / 10)

        return res

if __name__ == '__main__':
    Solu = Solution()
    print(Solu.addStrings("99","8"))