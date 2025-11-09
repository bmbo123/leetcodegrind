class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        F, S = 0,0
        res = ""

        while F < len(word1) and S < len(word2):
            res += word1[F]
            res += word2[S]
            F+= 1
            S+= 1
        
        if F < len(word1):
            res += word1[F:]
        else:
            res += word2[S:]
        return res




        