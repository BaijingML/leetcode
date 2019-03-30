class Solution:
    def uncommonFromSentences(self, A, B):
        A_set = self.counter_frequence(A)
        B_set = self.counter_frequence(B)
        result = []
        for i in A_set:
            if A_set[i] > 1:
                continue
            else:
                if i not in B_set:
                    result.append(i)
        for i in B_set:
            if B_set[i] > 1:
                continue
            else:
                if i not in A_set:
                    result.append(i)
        return result

    def counter_frequence(self, A):
        A_set = {}
        A_list = A.split(' ')
        for i in range(len(A_list)):
            if A_list[i] in A_set:
                A_set[A_list[i]] += 1
            else:
                A_set[A_list[i]] = 1
        return A_set

if __name__ == '__main__':
    Solu = Solution()
    print(Solu.uncommonFromSentences("apple apple", "banana"))