class Solution {
public:
    int singleNumber(vector<int>& nums) {
        map<int, int> M;
        for(int i = 0; i < nums.size(); i++){
            auto it = M.find(nums[i]);
            if(it != M.end()){
                M[nums[i]] += 1;
            }else{
                M[nums[i]] = 1;
            }
       }
       for(auto it = M.begin(); it != M.end(); ++it){
            if(it->second == 1){
                return it->first;
            }
       }
       return -1;
    }
};