class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)
        for num in seen:
            if num - 1 not in seen:
                curr = 1
                n = num + 1
                while n in seen:
                    curr += 1
                    n += 1
                longest = max(longest, curr)
        return longest

        