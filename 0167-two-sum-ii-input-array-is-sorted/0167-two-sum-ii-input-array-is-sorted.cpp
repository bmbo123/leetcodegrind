class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int L = 0;
        int R = numbers.size()-1;
        while(L < R){
            if(numbers[L] + numbers[R] == target){
                return vector<int>{L+1, R+1};
            }else if(numbers[L]+numbers[R] > target){
                R--;
            }else if(numbers[L]+ numbers[R]< target){
                L++;
            }
        }
        return vector<int> {};
    }
};