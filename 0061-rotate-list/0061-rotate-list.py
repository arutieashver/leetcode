# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        last_node = head  
        total_nodes = 1 

        while last_node.next:
            total_nodes += 1
            last_node = last_node.next

        last_node.next = head
        k = k % total_nodes

        if k == 0:
            last_node.next = None  
            return head            

        steps_to_new_tail = total_nodes - k - 1
        new_tail_candidate = head 

        for _ in range(steps_to_new_tail): 
            new_tail_candidate = new_tail_candidate.next

        new_head = new_tail_candidate.next

        # Step 5: Break the Circle and Return
        # Set the new tail's next pointer to None to break the circle and terminate the list.
        new_tail_candidate.next = None

        # Return the new head of the rotated list.
        return new_head