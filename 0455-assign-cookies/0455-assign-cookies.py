class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        print(g)
        print(s)
        count = 0
        check = 0
        for i in range(len(s)):
            if check < len(g):
                if s[i] >= g[check]:
                    count += 1
                    check += 1
        return count