class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string r = "";
        int number;
        // ab // rqw
        if(word1.length() > word2.length()){
            number = word1.length();
        }else{
            number = word2.length();
        }
        for(int i = 0; i < number ; i++){

            if(word1.length() > i){
                r += word1[i];
            }
            if(word2.length()> i){
                r += word2[i];
            }

        }
        return r;
    }
};