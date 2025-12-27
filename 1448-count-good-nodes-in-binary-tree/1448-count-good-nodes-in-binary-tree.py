# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # max is the node visited previously
        def helper(root,m):
            if root == None:
                return 0
            if root.val  >= m:
                m = max(root.val,m)
                return helper(root.left,m) + helper(root.right, m) + 1
            else:
                return helper(root.left, m) + helper(root.right, m)
        return helper(root, root.val)

            
            
