class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = 0
        L , R = 0, 0
        seen = set()
    ## use for loop as R
    # ACBDBE

        while R < len(s):
            if s[R] in seen:
                curr = max(curr, R-L)
                seen.remove(s[L])
                L += 1
            else:
                seen.add(s[R])
                R+= 1
        curr = max(curr, R-L)
        return curr







            