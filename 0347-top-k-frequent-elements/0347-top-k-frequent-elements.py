class Solution:
    from collections import Counter
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        #print(freq)
        max_heap = []
        result = []
        
        
        
        for number,freq in freq.items():
            heapq.heappush(max_heap,(freq*-1,number))
        
        for i in range(k):
            result.append(heapq.heappop(max_heap)[1])
            
        return result
        
        
        
        
        
        