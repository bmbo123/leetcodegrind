class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = Counter(nums)
        res = []
        while k> 0 and seen:
            x = max(seen, key = seen.get)
            res.append(x)
            del seen[x]
            k -= 1
        
        return res
            



            
        
