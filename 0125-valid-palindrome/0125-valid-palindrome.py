class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ""

        for char in s:
            if char.isalnum():
                p += char
        L , R = 0, len(p) - 1
        p = p.lower()
        while L < R:
            if p[L] == p[R]:
                L += 1
                R -= 1
            else:
                return False

        return True
 