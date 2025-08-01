"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None

        leftmost = root

        while leftmost.left:
            cur = leftmost

            while cur:
                cur.left.next = cur.right

                if cur.next:
                    cur.right.next = cur.next.left

                cur = cur.next

            leftmost = leftmost.left

        return root