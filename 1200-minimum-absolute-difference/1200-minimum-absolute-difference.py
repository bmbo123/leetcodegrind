class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        minDiff = float('inf')

        arr.sort()
        res = []

        for i in range(1,len(arr)):
            d = arr[i]-arr[i-1]
            if d < minDiff:
                minDiff = arr[i]-arr[i-1]
                res = []
                res.append([arr[i-1], arr[i]])
            elif d == minDiff:
                res.append([arr[i-1],arr[i]])
        
        return res



        