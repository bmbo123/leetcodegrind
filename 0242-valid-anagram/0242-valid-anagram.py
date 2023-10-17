class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqMap1 = {}
        freqMap2 = {}

        for i in range(len(s)):
            if s[i] not in freqMap1:
                freqMap1[s[i]] = 1
            else:
                freqMap1[s[i]] += 1               
            
        for i in range(len(t)):
            if t[i] not in freqMap2:
                freqMap2[t[i]] = 1
            else:
                freqMap2[t[i]] += 1   

        return freqMap1 == freqMap2            
            