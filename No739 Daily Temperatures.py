class Solution:
    def dailyTemperatures(self, T):
        if not T:
            return []
        n = len(T)
        near_max = []
        result = [0] * n

        for i in range(n-1, -1, -1):
            print(near_max)

            while near_max and T[i] >= T[near_max[-1]]:
                near_max.pop()
            if near_max:
                result[i] = near_max[-1] - i
            near_max.append(i)
        return result

if __name__ == "__main__":
    solu = Solution()
    print(solu.dailyTemperatures([73,74,75,71,69,72,76,73]))