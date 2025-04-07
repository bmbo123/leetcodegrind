class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        r = s[::-1]
        print(r)

        for i in range(2, len(s)):
            test = s[i-2:i]
            print(test)
            if test in r:
                return True
        return False

        