class Solution {
    public double findMaxAverage(int[] nums, int k) {
        //sliding window, subarray size k, average
        //
        double currAverage = 0;
        double currSum = 0;
        for(int i = 0; i < k; i++) {
            currSum += nums[i];   
        }
        
        currAverage = currSum/k;
        double ans = currAverage;
        for (int j = k; j < nums.length; j++) {
            currSum  = currSum + nums[j] - nums[j - k];
            currAverage = currSum/k;
            ans = Math.max(ans, currAverage);
        }
        
        return ans;
    }
}
