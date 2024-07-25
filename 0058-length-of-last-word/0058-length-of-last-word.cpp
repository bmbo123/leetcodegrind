class Solution {
public:
    int lengthOfLastWord(string s) {
int L = s.length();

        // Skip trailing spaces
        while (L > 0 && s[L - 1] == ' ') {
            L--;
        }

        int R = L;

        // Find the length of the last word
        while (L > 0 && s[L - 1] != ' ') {
            L--;
        }

        return R - L;
    }
};