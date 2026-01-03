import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #[2,7,4,1,8,1] -> 0th - 2 , 1st-7, 2nd-4....
        #max heap
        max_heap = []
    
        for stone in stones:
            heapq.heappush(max_heap,stone * -1) #for the max heap (where im pushing,what im pushing)
        
        while max_heap and len(max_heap) > 1:
            y = heapq.heappop(max_heap) * -1
            x = heapq.heappop(max_heap) * -1
            
            if x == y:
                continue
            else:
                y = y-x
                heapq.heappush(max_heap,y * -1)  
        if max_heap:
            return max_heap[-1] * -1
        else:
            return 0           
            
        
        