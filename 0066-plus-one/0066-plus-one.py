class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = True

        tes = set(digits)
        if len(tes) == 1 and 9 in tes:
            res = []
            for i in range(len(digits)+1):
                if i == 0:
                    res.append(1)
                else:
                    res.append(0)
            return res
        
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                if flag:
                    digits[i] = 0
            elif flag :
                digits[i] += 1
                flag = False

        return digits

        