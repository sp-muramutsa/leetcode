class Solution {
    public int longestOnes(int[] nums, int k) {
        //subarray, sliding windonw, nums, k, flip k 0's
        //record the number of zeros
        int left = 0;
        int currZeroes = 0;
        int ans = 0; //size of the subarray
        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) {
                currZeroes++;
            }
            
            while(currZeroes > k) {
                if (nums[left] == 0) {
                    currZeroes--;
                }
                left++;
            }
            
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
