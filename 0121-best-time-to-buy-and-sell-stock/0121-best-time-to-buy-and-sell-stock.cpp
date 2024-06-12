class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max = 0;
        int low = 0;
        for(int i = 1; i < prices.size(); i++){
            if(prices.at(i) < prices.at(low)){
                low = i;
            }
            if(prices.at(i) - prices.at(low) > max){
                max = prices.at(i) - prices.at(low);
            }
        }
        return max;
    }
};