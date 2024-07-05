class Solution {
public:
    bool isPalindrome(string s){
        int L = 0;
        int R = s.length()-1;
        while(L < R){
            if(s[L] != s[R]){
                return false;
            }
            L++;
            R--;
            
        }
        return true;
    }
    bool validPalindrome(string s) {
        int L = 0;
        int R = s.length()-1;
        while(L < R){
            string ss = s;
            if(s[L] != s[R]){
                return isPalindrome(ss.erase(L,1)) || isPalindrome(s.erase(R,1));
            }
            L++;
            R--;
        }
        return true;
    }
};