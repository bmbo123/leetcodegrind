class Solution:
    def isPalindrome(self, s: str) -> bool:
        norm = ""
        for char in s:
            if char.isalnum():
                norm += char
        norm = norm.lower()
        L, R = 0, len(norm)-1

        while L < R:
            if norm[L] != norm[R]:
                return False
            L += 1
            R -= 1
        return True
        