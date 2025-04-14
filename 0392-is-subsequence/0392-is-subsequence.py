class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True
        index = 0
        for i in range(len(t)):
            if index == len(s):
                return True
            if s[index] == t[i]:
                index += 1
        return index == len(s)





