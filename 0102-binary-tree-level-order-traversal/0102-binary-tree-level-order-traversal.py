# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        def bfs(root):
            queue = []
            queue.append(root)
            res = []
            while queue:
                curr = []
                n = len(queue)
                for i in range(n):
                    node = queue.pop(0)
                    curr.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                res.append(curr)
            return res
        return bfs(root)
                