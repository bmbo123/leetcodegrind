class Solution:
    def check(self,first, second):
        for val in second:
            if val in first and first[val] >= second[val]:
                continue
            else:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        final = ""
        L, R = 0,0
        con = Counter(t)
        test = Counter()
        while R < len(s):
            test[s[R]] += 1
            while self.check(test, con):
                if not final:
                    final = s[L:R+1]
                else:
                    if len(final) > len(s[L:R+1]):
                        final = s[L:R+1]
                test[s[L]] -= 1
                L+=1
            R+=1
        return final