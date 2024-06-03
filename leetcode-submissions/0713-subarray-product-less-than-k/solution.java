class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        //sliding window
        if (k == 0) { return 0; }
        int ans = 0;
        int curr = 1;
        int left = 0; 
        int n = nums.length;
        for(int right = 0; right < n; right++) {
            curr *= nums[right];
            while(curr >= k && left <= right) {
                curr = curr/nums[left];
                left++;
            }
            ans += right - left + 1;
        }
        return ans;
    }
}
