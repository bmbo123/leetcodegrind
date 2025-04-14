class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        print(s)
        print(g)
        j = 0 
        for i in range(len(s)):
            if i <= len(g)- 1:
                if s[i] >= g[j]:
                    count += 1
                    j += 1
        return count


