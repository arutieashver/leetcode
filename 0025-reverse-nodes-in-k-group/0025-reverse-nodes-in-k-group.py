
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        dummy = ListNode()
        new = dummy
        current = head
        proceed = None
        while current:
            stack.append(current.val)
            if len(stack) == k:
                stack = reversed(stack)
                for i in stack:
                    dummy.next = ListNode(i)
                    dummy = dummy.next
                stack = []
                proceed = current.next
            current = current.next
        dummy.next = proceed
        return new.next