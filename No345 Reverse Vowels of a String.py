class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiou'
        vowels_index = []
        s_list = [i for i in s]
        s_vowels = ''
        for i in range(len(s)):
            if s[i] in vowels:
                vowels_index.append(i)
                s_vowels += s[i]
        for j in range(len(s_vowels)):
            s_list[vowels_index[len(s_vowels)-j-1]] = s_vowels[j]
        return ''.join(s_list)
print(Solution.reverseVowels(Solution, "hello"))