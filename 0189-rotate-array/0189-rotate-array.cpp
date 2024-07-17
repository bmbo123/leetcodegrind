class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        vector<int> answer(nums.size());
        for(int i = 0 ; i < nums.size(); i++){
            int index = (i+k)%nums.size();
            answer[index] = nums[i];
        }
        for(int i = 0; i < nums.size(); i++){
            nums[i]  = answer[i];
        }
    }
};