# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = slow.next

        while fast is not None and fast.next is not None:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
        