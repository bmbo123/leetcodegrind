from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        m = 0
        L = 0
        best = 0

        for i in range(len(s)):
            freq[s[i]] += 1
            m = max(m, freq[s[i]] )

            while (i-L+1) - m > k:
                freq[s[L]] -=1
                L += 1
            best = max(best, i-L +1)
        return best



