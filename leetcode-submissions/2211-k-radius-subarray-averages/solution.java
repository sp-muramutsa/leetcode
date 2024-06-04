class Solution {
    public int[] getAverages(int[] nums, int k) {
        //if k is zero, also checking the first and last k elements of the array (set to -1)
        // denominator will be 2k + 1
        // 
        
        /*
        * [7,4,3,9,1,8,5,2,6], k = 3
        * [7, 11, 14, 23, 24, 32, 37, 39, 45]
        * [-1, -1, -1, ]
        */
        
        int n = nums.length;
        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        if (k == 0) { return nums; }
        if(2*k >= n) {
            return ans;
        }
        
        long[] prefixSums = new long[n];
        prefixSums[0] = nums[0];
        for(int i = 1; i < n; i++) {
            prefixSums[i] = prefixSums[i - 1] + nums[i];
        }

        // int currSum = prefixSums[2*k];
        ans[k] = (int) (prefixSums[2*k]/((2*k) + 1));
        for(int l = k + 1; l < n - k; l++) {
            long sum = prefixSums[l + k] - prefixSums[l - k - 1];
            ans[l] = (int) (sum/((2*k) + 1));
        }
        return ans;
    }
}
