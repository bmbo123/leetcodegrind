class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        for(int i = 0; i < arr.size(); i++){
            if(arr[i] == 0){
                int j = arr.size() - 1;
                for(; j >= i+1; j--){
                    arr[j] = arr[j-1];
                }
                            i++;
            }
        }
    }
};