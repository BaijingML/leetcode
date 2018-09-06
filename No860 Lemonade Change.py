class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        receiver_dict = {5:0, 10:0, 20:0}
        for i in bills:
            receiver_dict[i] += 1
            if i == 5:
                continue
            elif i == 10:
                receiver_dict[5] -= 1
                if receiver_dict[5] == -1:
                    return False
            else:
                if receiver_dict[5] < 1:
                    return False
                if receiver_dict[10] == 0 and receiver_dict[5] >= 3:
                    receiver_dict[5] -= 3
                elif receiver_dict[10] > 0 and receiver_dict[5] > 0:
                    receiver_dict[10] -= 1
                    receiver_dict[5] -= 1
                else:
                    return False
        return True