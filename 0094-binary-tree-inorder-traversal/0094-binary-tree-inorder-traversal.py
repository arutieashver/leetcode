# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
         nodes = []
         result = []

         while root or nodes:
            while root:
                nodes.append(root)
                root = root.left
            
            root = nodes.pop()
            result.append(root.val)

            root = root.right
        
         return result   