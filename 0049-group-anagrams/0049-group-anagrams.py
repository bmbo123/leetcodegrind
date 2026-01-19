class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}

        for i in range(len(strs)):

            norm = "".join(sorted(list(strs[i])))
            if norm in seen:
                seen[norm].append(strs[i])
            else:
                seen[norm] = [strs[i]]
        
        res = []
        print(seen)
        for key in seen:
            res.append(seen[key])
        
        return res

