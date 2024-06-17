class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        vector<int> nums2(nums.size());
        for(int i = 0; i < nums.size(); i++){
            int index = (i+k) % nums.size();
            nums2[index] = nums[i];
        }
        for(int i = 0; i < nums.size();i++){
            nums[i] = nums2[i];
        }
    }
};