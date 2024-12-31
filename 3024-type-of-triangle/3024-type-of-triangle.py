class Solution:
    def triangleType(self, nums: List[int]) -> str:
        equal = len(set(nums))
        
        a, b, c = sorted(nums)
        if a + b <= c:
            return "none"

        if equal == 2:
            return "isosceles"
        if equal == 1:
            return "equilateral"
        

        return "scal"