class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 1;
        int res = nums[0];
        for(int i = 0; i < nums.size(); i++){
            if(i != 0){
                if(count == 0){
                    res = nums[i];
                    count++;
                }else if(nums[i] == res){
                    count++;
                }else{
                    count--;
                }
            }
        }
        return res;
    }
};