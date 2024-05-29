class Solution {
public:
    int maxSubArray(vector<int>& nums) 
    {
        int sum = 0;
        int best = INT_MIN;
        int length = nums.size();

        for(int i = 0; i < length; i++)
        {
            sum = max(nums[i], sum + nums[i]);
            best = max(best, sum);
        }
        return best;
    }
};
