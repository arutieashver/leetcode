# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def depthLeft(node):
            depth = 0
            while node: 
                depth +=1
                node = node.left
            return depth
        
        def depthRight(node):
            depth = 0
            while node: 
                depth += 1
                node = node.right
            return depth

        leftdepth = depthLeft(root.left)
        rightdepth = depthRight(root.right)

        if leftdepth == rightdepth:
            return 2 ** (leftdepth + 1) -1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
