class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int L = 0;
        int R = nums.size()-1;

        while(L  < R){
            if(nums[L] %2 !=0 && nums[R] %2 == 0){
                swap(nums[L], nums[R]);
                L++;
                R--;

            }else if(nums[L] %2 != 0 && nums[R] % 2 != 0){
                R--;
            }else{
                L++;
            }
        }
            return nums;
    }
};