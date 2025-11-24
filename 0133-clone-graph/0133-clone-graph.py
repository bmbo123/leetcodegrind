"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        seen = {}
        def dfs(node):
            new = Node(node.val)
            seen[node.val] = new

            for neighbor in node.neighbors:
                if neighbor.val not in seen:
                    dfs(neighbor)
                new.neighbors.append(seen[neighbor.val])
            return new
        
        return dfs(node)

                    


