class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        print(len(s))
        for i in range(len(s)):
            x = {}
            curr = 0
            for j in range(i, len(s)):
                if s[j] in x:
                    break
                else:
                    x[s[j]] = 1
                    curr += 1 
            count = max(curr, count)
        
        return count 
                    

