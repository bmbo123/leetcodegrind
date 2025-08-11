import heapq
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        kids = 0
        max_g = [-greed for greed in g]
        max_s = [-size for size in s]

        heapq.heapify(max_g)
        heapq.heapify(max_s)

        while max_g and max_s:
            if -max_g[0] <= -max_s[0]:
                kids += 1
                heapq.heappop(max_g)
                heapq.heappop(max_s)
            else:
                heapq.heappop(max_g)
        
        return kids