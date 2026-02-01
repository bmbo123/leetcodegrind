# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = deque()

        q.append(root)
        res = []
        if not root:
            return []

        while q:

            l = len(q)
            cres = []


            for i in range(l):
                curr = q.popleft()
                cres.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            res.append(cres)
        return res[::-1]

        