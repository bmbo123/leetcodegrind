class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[curr] = nums[i]
                curr += 1
                count +=1
        
        return count
        
        