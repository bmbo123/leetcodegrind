class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(nums, target, l, h):
            if l == h and nums[l] != target:
                return  -1

            mid = (l + h) // 2

            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if target <= nums[mid] and target >= nums[l]:
                    return bs(nums, target, l, mid -1)
                else:
                    return bs(nums, target, mid +1, h)
            else:
                if target >= nums[mid] and target <= nums[h]:
                    return bs(nums, target, mid +1, h)
                else:
                    return bs(nums, target, l, mid -1)
            return bs(nums, target, l, h)
        return bs(nums, target, 0, len(nums)-1)
