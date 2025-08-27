class Solution:
    def frequencySort(self, s: str) -> str:
        x = Counter(s)
        arr = []
        for char in s:
            arr.append((-x[char], char))
        print(arr)
        heapq.heapify(arr)
        res = ""
        while arr:
           F = heapq.heappop(arr)
           res += F[1]
        return res
        
