class Solution:
    def twoSum(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        if numbers[0] > target:
            return []
        pre = 0
        post = len(numbers) - 1
        while pre < post:
            if numbers[pre] + numbers[post] == target:
                return [pre + 1, post + 1]
            elif numbers[pre] + numbers[post] < target:
                pre += 1
            else:
                post -= 1