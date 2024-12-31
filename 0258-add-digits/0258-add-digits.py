class Solution:
    def addDigits(self, num: int) -> int:
        while num > 10:
            x = 0
            for char in str(num):
                x += int(char)
            num = x
        return num
                