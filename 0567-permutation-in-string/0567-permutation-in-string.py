class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        fm = {}
        for char in s1:
            if char in fm:
                fm[char] += 1
            else:
                fm[char] = 1
        l = 0
        for r in range(len(s1),len(s2)+1):
            check = {}
            print(r)
            for char in s2[l:r]:
                if char in check:
                    check[char] += 1
                else:
                    check[char] = 1
            print(check)
            if check == fm:
                print(check)
                print(fm)
                return True
            l += 1
        print(fm)
        return False
        


