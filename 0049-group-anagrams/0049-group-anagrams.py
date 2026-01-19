class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashmap problem Freq: word
        Anagram =  defaultdict(list)
        
        for string in strs:
            countlist = [0]*26
            for ch in string: 
                countlist[ord(ch) - ord('a')] +=1
            Anagram[tuple(countlist)].append(string)
        return list(Anagram.values())