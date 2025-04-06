class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tes = set(nums)
        longest = 0

        for num in tes:  # Use set to avoid duplicates
            if num - 1 not in tes:  # Start of a new sequence
                length = 0
                while num + length in tes:
                    length += 1
                longest = max(longest, length)
        
        return longest
