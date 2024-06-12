class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> M;
        map<char, int> F;
        for(int i = 0; i < s.length(); i++){
            M[s[i]]++;
        }
        for(int i = 0; i < t.length(); i++){
            F[t[i]]++;
        }
        return M == F;
    }
};