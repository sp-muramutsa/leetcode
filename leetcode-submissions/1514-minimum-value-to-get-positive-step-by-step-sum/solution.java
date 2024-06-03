class Solution {
    public int minStartValue(int[] nums) {
        //prefix sums, if the smallest is < 1, return 1 - that
        // int[] prefixSums = new int[nums.length];
        int prevSum = nums[0];
        int smallestPrefix = prevSum;
        for(int i = 1; i < nums.length; i++) {
            prevSum += nums[i];
            if (prevSum < smallestPrefix) {
                smallestPrefix = prevSum;
            }
        }
        if (smallestPrefix < 1) {
            return 1 - smallestPrefix;
        }
        return 1; 
    }
}
