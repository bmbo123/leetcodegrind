class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int L = 0;
        int R = nums.size()-1;
        while(L<=R){
            int m = (L+R)/2;
            if(nums[m] == target){
                return m;
            }else if(nums[m] > target){
                R = m-1;
            }else if(nums[m] < target){
                L = m+1;
            }
        }
        return L;
    }
};