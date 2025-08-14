class Solution:
    def largestGoodInteger(self, num: str) -> str:
        m = ""
        for i in range(2,len(num)):
            x = num[i-2:i+1]
            r = set(x)
            if len(r) == 1:
                if x > m:
                    m = x
        return m
        