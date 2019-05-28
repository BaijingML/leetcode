class Solution:
    def countBits(self, num):
        result = [0]
        for i in range(2, num+1):
            print(result[int(i/2)] + i % 2)
            result.append(result[int(i/2)] + i % 2)
        return result