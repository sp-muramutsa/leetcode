class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        //sliding window?

        int ans = Integer.MAX_VALUE; //min length
        int curr = 0; //window's sum
        int left = 0;
        for(int right = 0; right < nums.length; right++) {
            curr += nums[right];
            while (curr >= target && left <= right) {
                ans = Math.min(ans, right - left + 1);
                curr -= nums[left];
                left++;
            }
        }
        if(ans == Integer.MAX_VALUE) {return 0;}
        return ans;
    }
}
