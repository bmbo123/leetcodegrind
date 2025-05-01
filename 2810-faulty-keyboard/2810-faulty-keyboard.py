class Solution:
    def finalString(self, s: str) -> str:
        final = []
        s = list(s)
        print(s)
        for i in range(len(s)):
            if s[i] == "i":
                final = reversed(final)
                final = list(final)
            else:
                final.append(s[i])
        return "".join(final)
            