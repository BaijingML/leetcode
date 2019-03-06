class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slow = fast = head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next
                if slow == fast:
                    break
            else:
                return None
        if not fast:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow