class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = "".join(x for x in s if x.isalnum())
        r = r.lower()
        return r[::-1] == r

