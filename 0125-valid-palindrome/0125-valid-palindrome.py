class Solution:
    def isPalindrome(self, s: str) -> bool:
        real = "" 
        for i in s:
            if i.isalnum():
                real += i
        real = real.lower()
        r = real[::-1]
        return r==real
