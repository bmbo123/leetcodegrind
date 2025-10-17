class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)
        buckets = []
        for i in range(len(nums)):
            buckets.append([])
        for key, val in x.items():
            buckets[val-1].append(key)

        res = []
        for i in range(len(buckets)):
            res.extend(buckets[i-1])
        
        return res[-k:]
        
        
