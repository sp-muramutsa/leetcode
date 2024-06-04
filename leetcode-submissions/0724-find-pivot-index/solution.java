class Solution {
    public int pivotIndex(int[] nums) {
        /**
            prefixsum... for each point do check the sum on both ends... 
         */

        int[] prefixSum = new int[nums.length];
        prefixSum[0] = nums[0];

        for(int i = 1; i < nums.length; i++) {
            prefixSum[i] = prefixSum[i - 1] + nums[i];
        }

        
        for(int j = 0; j < nums.length; j++) {
            int leftSum = j == 0 ? 0 : prefixSum[j - 1];
            int rightSum = prefixSum[nums.length - 1] - prefixSum[j];
            if (leftSum == rightSum) { return j; }
        }
        return -1;   
    }
}
