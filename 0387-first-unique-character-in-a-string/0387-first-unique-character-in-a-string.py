class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}

        for x in range(len(s)):
            if s[x] in dict:
                count, index = dict[s[x]]
                dict[s[x]] = (count+1, index)
            else:
                dict[s[x]] = (1, x)

        for i,(x,y) in dict.items():

            if x == 1:
                return y

        return -1