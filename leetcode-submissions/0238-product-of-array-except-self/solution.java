class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix = new int[nums.length];
        int prefixTotal = nums[nums.length - 1];
        prefix[nums.length - 1] = prefixTotal;
        for(int i  = nums.length - 2; i >= 0; i--) {
            prefixTotal *= nums[i];
            prefix[i] = prefixTotal;
        }

        int[] suffix = new int[nums.length];
        int suffixTotal = nums[0];
        suffix[0] = suffixTotal;
        for(int i  = 1; i < nums.length; i++) {
            suffixTotal *= nums[i];
            suffix[i] = suffixTotal;
        }

        int[] output = new int[nums.length];
        for(int i = 1; i < nums.length - 1; i++) {
            output[i] = suffix[i - 1] * prefix[i + 1];
        }
        output[0] = prefix[1];
        output[nums.length - 1] = suffix[nums.length - 2];
        return output;
    }
}
