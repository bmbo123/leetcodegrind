class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            norm = "".join(sorted(list(word)))

            if norm in groups:
                groups[norm].append(word)
            else:
                groups[norm] =  [word]
        res = []
        for key, value in groups.items():
            res.append(value)
        
        return res

            
        