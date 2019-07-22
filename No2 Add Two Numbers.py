# class Solution(object):
    # def addTwoNumbers(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     if not l1 and not l2: return None
    #     if not l1: return l2
    #     if not l2: return l1
    #     order = 0
    #     len_l1 = self.count_len(l1)
    #     len_l2 = self.count_len(l2)
    #     if len_l1 < len_l2:
    #         head = l2
    #     else:
    #         head = l1
    #     node = head
    #     while l1 and l2:
    #         n = l1.val + l2.val
    #         if n >= 10:
    #             head.val = n - 10
    #             order = 1
    #         else:
    #             head.val = n + order
    #             order = 0
    #         head = head.next
    #         l1 = l1.next
    #         l2 = l2.next
    #     print(l1.val, l2.val,head.val)
    #     while l1 or l2:
    #         head.val = head.val + order
    #         order = 0
    #         head = head.next
    #     return node
    # def count_len(self, l):
    #     count = 0
    #     while l:
    #         count += 1
    #         l = l.next
    #     return count

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        temp = l1
        indicate = ListNode(0)
        while l1 and l2:
            l1, indicate = self.add(l1, l2, indicate)
            temp = l1
            l1, l2 = l1.next, l2.next
        if not l1 and not l2 and indicate != 0:
            temp.next = indicate
        elif l1:
            l1.val = l1.val + indicate.val
        elif l2:
            l2.val = l2.val + indicate.val
            l1 = l2
        return head

    def add(self, l1, l2, indicate):
        if not l1:
            return l2
        if not l2:
            return l1
        value = l1.val + l2.val + indicate.val
        l1.val = value % 10
        if value > 9:
            indicate.val = 1
        else:
            indicate.val = 0
        return l1, indicate

if __name__ == "__main__":
    solu = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(8)
    l2 = ListNode(0)
    solu.addTwoNumbers(l1, l2)