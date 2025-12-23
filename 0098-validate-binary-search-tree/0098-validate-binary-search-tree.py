# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #return self.valid(root,float('-inf'),float('inf'))

        def valid(root,minn,maxx):
            if root == None:
                return True
            if root.val <= minn or root.val >= maxx:
                return False
        
            return valid(root.left,minn,root.val) and valid(root.right,root.val,maxx)
        return valid(root,float('-inf'),float('inf'))