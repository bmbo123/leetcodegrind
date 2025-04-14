class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ml = 0

        for i in range(len(s)):
            sett = set()
            for j in range(i,len(s)):
                if s[j] in sett:
                    ml = max(ml, len(sett))
                    break
                else:
                    sett.add(s[j])
                    ml = max(ml, len(sett)) 
            print(sett)
        return ml






        