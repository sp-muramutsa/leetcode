class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        /**
            k odd numbers in a subarray
        */

        Map<Integer, Integer> freqs = new HashMap<>();
        freqs.put(0, 1);
        int ans = 0;
        int curr = 0;
        for (int i = 0; i < nums.length; i++) {
            curr += nums[i] % 2;
            ans += freqs.getOrDefault(curr - k, 0);
            freqs.put(curr, freqs.getOrDefault(curr, 0) + 1);
        }
        return ans;
    }
}
