# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        curr = []
        res = []
        self.path(root,targetSum,curr, res)

        return res
    
    def path(self,root, targetSum, curr, res):
        if root is None:
            return False
        curr.append(root.val)
        if root.left is None and root.right is None and sum(curr) == targetSum:
            print(sum(curr),curr)
            res.append(curr[:])
            print(res)
        self.path(root.left, targetSum, curr, res)
        self.path(root.right, targetSum, curr, res)
        curr.pop()
        













        