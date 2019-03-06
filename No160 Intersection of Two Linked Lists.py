# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1 = self.getLength(headA)
        l2 = self.getLength(headB)
        if l1 >= l2:
            headlong = headA
            headshort = headB
        else:
            headlong = headB
            headshort = headA
        for i in range(abs(l1 - l2)):
            headlong = headlong.next
        while headlong and headshort:
            if headlong == headshort:
                return headlong
            headlong = headlong.next
            headshort = headshort.next
        return None

    def getLength(self, head):
        l = 0
        while head:
            head = head.next
            l += 1
        return l