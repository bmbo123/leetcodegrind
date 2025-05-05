class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        seen = {}
        count = 0
        for i in range(len(nums)):
            x = nums[i]
            x = str(x)
            x = list(x)
            test = reversed(x)
            test = "".join(test)
            test = int(test)
            print(test)
            r = nums[i] - test
            if r in seen:
                count += seen[r]
                seen[r] += 1
            else:
                seen[r] = 1
        mod = 10**9 + 7
        print(mod)
        return count % mod

            