class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2: return None
        if not l1: return l2
        if not l2: return l1
        order = 0
        len_l1 = self.count_len(l1)
        len_l2 = self.count_len(l2)
        if len_l1 < len_l2:
            head = l2
        else:
            head = l1
        node = head
        while l1 and l2:
            n = l1.val + l2.val
            if n >= 10:
                head.val = n - 10
                order = 1
            else:
                head.val = n + order
                order = 0
            head = head.next
            l1 = l1.next
            l2 = l2.next
        print(l1.val, l2.val,head.val)
        while l1 or l2:
            head.val = head.val + order
            order = 0
            head = head.next
        return node
    def count_len(self, l):
        count = 0
        while l:
            count += 1
            l = l.next
        return count