class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        L = 0
        longest = 0

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[L])
                L +=1
            seen.add(s[i])
            longest = max(longest, i-L+1)
    
        return longest
