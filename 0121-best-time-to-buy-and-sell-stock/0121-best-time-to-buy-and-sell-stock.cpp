class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max = 0;
        int low = prices[0];
        for(int i = 1; i < prices.size(); i++){
            if(prices[i] - low > max){
                max = prices[i] - low;
            }else if(prices[i]< low){
                low = prices[i];
            }
        }
        return max;
    }
};