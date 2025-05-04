class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen = {}
        count = 0
        for i in range(len(dominoes)):
            test = tuple(sorted(dominoes[i]))
            if test in seen:
                count += seen[test]
                seen[test] += 1
            else:
                seen[test] = 1
        return count