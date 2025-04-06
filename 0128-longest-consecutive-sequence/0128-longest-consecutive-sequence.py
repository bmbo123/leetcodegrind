class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tes = set(nums)
        longest = 0
        for num in tes:
            if (num -1) not in tes:
                length = 0
                while (num + length) in tes:
                    length += 1
                longest = max(length,longest)
        return longest
                












        

        