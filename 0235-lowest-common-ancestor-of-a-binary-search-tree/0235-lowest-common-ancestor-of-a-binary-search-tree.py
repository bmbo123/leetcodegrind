# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def bfs(root, p,q):
            if p.val > root.val and q.val > root.val:
                return bfs(root.right,p,q)
            elif root.val > p.val and q.val < root.val:
                return bfs(root.left,p,q)
            else:
                return root
        return bfs(root,p,q)
            