class Solution {


    public int[] twoSum(int[] nums, int target) {
        int lo = 0; int hi = nums.length - 1;
        int[] ans = new int[2];

        while (lo < hi) {
            int sum  = nums[lo] + nums[hi];
            if (sum < target) {
                lo++;
            } else if (sum > target) {
                hi--;
            } else {
                ans[0] = lo + 1;
                ans[1] = hi + 1;
                return ans;
            }
        }
        return ans;
    }
}
