class Solution:
    def maxProduct(self, n: int) -> int:
        s = list(str(n))              
        s = sorted(s)                 
        s = [int(d) for d in s]
        m = 0

        for i in range(1,len(s)):
            m = max(s[i] * s[i-1], m)
        return m