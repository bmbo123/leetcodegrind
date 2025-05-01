class Solution:
    def romanToInt(self, s: str) -> int:
        final = 0
        ## IV
        nums = {"I":1, "V":5, "X":10,"L":50,"C":100, "D":500,"M":1000}
        final += nums[s[-1]]
        for i in range(len(s)-2, -1,-1):
            if nums[s[i]] < nums[s[i+1]]:
                final -= nums[s[i]]
            else:
                final += nums[s[i]]
        return final

