class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        x = Counter(tasks)
        arr = []
        heapq.heapify(arr)
        for key in x:
            heapq.heappush(arr,( -x[key],key))
        queue = deque()
        time = 0
        while arr or queue:
            if arr:
                freq,val = heapq.heappop(arr)
                freq += 1
                if freq != 0:
                    queue.append([freq, val, time+n])
            if queue and queue[0][2] == time:
                freq, val, _ = queue.popleft()
                heapq.heappush(arr, (freq,val))
            time += 1
        return time
            
        