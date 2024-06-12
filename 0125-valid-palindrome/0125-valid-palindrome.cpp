class Solution {
public:
    bool isPalindrome(string s) {
        string real = "";
        for(int i = 0; i < s.length(); i++){
            if(isalnum(s[i])){
                real += tolower(s[i]);
            }
        }

    int counter = real.length()-1;

    for(int i = 0; i < real.length(); i++){
        if(real[counter]!=real[i]){
            return false;
        }
        counter--;
    }
    return true;
    }
};