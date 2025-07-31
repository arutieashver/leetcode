# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        values = []
        
        for head in lists:
            while head:
                values.append(head.val)
                head = head.next

        values.sort()
       
        for val in values:
            current.next = ListNode(val)
            current = current.next

        return dummy.next