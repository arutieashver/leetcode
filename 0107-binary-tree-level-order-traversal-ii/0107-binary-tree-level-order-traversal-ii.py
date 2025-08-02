# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = deque([root])
        while q:
            res.append([elem.val for elem in list(q)])
            for _ in range(len(q)):
                p = q.popleft()
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
        return res[::-1]