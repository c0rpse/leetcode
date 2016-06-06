#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None

        slow, fast = head, head
        while slow != None and fast != None and fast.next != None:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        if slow != fast:
            return None
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast

s  = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = head.next

h = s.detectCycle(head)
print h.val