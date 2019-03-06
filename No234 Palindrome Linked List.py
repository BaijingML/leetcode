class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        node = None
        while slow:
            temp = slow.next
            slow.next = node
            node = slow
            slow = temp
        while node:
            if head.val != node.val:
                return False
            node = node.next
            head = head.next
        return True