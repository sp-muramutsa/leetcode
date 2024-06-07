class Solution {
    public int largestUniqueNumber(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        for(int num: nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }
        int ans = -1;
        for(int num:nums) {
            if (counts.get(num) == 1 && num > ans) {
                ans = num;
            }
        }
        return ans;
    }
}
