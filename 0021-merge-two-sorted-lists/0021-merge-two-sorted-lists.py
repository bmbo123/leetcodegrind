# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1 and list2:
            return list2
        elif not list2 and list1:
            return list1
        node = ListNode()
        if list1.val > list2.val:
            node.val = list2.val
            list2 = list2.next
        else:
            node.val = list1.val
            list1 = list1.next
        dummy = node
        while list1 and list2:
            if list1.val > list2.val:
                dummy.next = list2
                list2 = list2.next
            else:
                dummy.next = list1
                list1 = list1.next
            
            dummy = dummy.next
        
        if not list1 and not list2:
            return node
        elif not list1 and list2:
            dummy.next = list2
        elif not list2 and list1:
            dummy.next = list1
        return node



            