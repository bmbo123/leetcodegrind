class Solution:
    def search(self, nums: List[int], target: int) -> int:

        L , R = 0, len(nums) -1

        while L <= R:

            mid  = (L + R) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L= mid +1
            else:
                R = mid - 1
        

        return -1
        