# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = []
        def helper(root,m):

            if root is None:
                return 
            
            if root.val >= m:
                print(root.val)
                count.append(root.val)
            m = max(root.val, m)

            helper(root.left,m)
            helper(root.right,m)
            

        helper(root,root.val)
        return len(count)



        