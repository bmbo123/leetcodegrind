class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = ""
        for char in s:
            if char.isalnum():
                f += char
        f=f.lower()
        r = f[::-1]
        return f == r
