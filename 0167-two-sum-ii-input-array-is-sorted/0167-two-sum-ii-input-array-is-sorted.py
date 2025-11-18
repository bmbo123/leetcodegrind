class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        L,R = 0, len(numbers)-1

        while L < R:
            x = numbers[L] + numbers[R]
            if x == target:
                return [L+1, R+1]
            elif x > target: 
                R -= 1
            else:
                L += 1
                


