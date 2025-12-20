class Solution:
    def reverseWords(self, s: str) -> str:
        x = s[::-1]
        res = ""

        x = x.split()
        print(x)
        for word in x:
            res += "".join(reversed(word))
            res += " "
        return res[:-1]



