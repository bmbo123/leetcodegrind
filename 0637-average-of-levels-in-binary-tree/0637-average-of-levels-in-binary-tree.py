# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()

        q.append(root)
        res = []

        while q:
            currsum = 0
            currlen = len(q)

            for i in range(currlen):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                currsum += curr.val

            res.append(currsum/ currlen)

        return res




            