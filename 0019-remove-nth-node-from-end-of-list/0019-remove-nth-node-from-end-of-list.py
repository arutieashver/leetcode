# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head
        dummy = current

        while current:
            count += 1
            current = current.next

        if count == n:
            head = head.next

        remove = count - n
        count = 0
        while dummy:
            count +=1
            if count == remove:
                dummy.next = dummy.next.next
                break
            dummy = dummy.next

        return head
