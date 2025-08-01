# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        head = root
        stack = []
        result = []

        while head or stack:
            if head:
                result.append(head.val)
                if head.left:
                    stack.append(head.left)
                head = head.right
            else:
                head = stack.pop()

        return result[::-1]        
     
        