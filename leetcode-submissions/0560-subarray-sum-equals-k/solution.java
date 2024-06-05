class Solution {
    public int subarraySum(int[] nums, int k) {
        //hashmap storing the frequency of the prefix

        Map<Integer, Integer> freqs = new HashMap<>();
        int ans = 0;
        int curr = 0;
        freqs.put(0, 1);
        for(int i = 0; i < nums.length; i++) {
            curr += nums[i];
            ans += freqs.getOrDefault(curr - k, 0);
            freqs.put(curr, freqs.getOrDefault(curr, 0) + 1);
        }
        return ans;
    }
}
