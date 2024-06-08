class Solution {
    public int findMaxLength(int[] nums) {
        // int ans = 0;
        // for(int begin = 0; begin < nums.length; begin++) {
        //     int zeroes = 0;
        //     int ones = 0;
        //     for(int end = begin; end < nums.length; end++) {
        //         if (nums[end] == 0) {
        //             zeroes++;
        //         } else {
        //             ones++;
        //         }
        //         if (zeroes == ones) {
        //             ans = Math.max(ans, end - begin + 1);
        //         }
        //     }
        // }
        // return ans;

        Map<Integer, Integer> counts = new HashMap<>();
        counts.put(0, -1);
        int curr = 0;
        int ans = 0;
        for(int i = 0; i < nums.length; i++) {
            curr += nums[i] == 0 ? -1 : 1;
            if(counts.containsKey(curr)) {
                ans = Math.max(ans, i - counts.get(curr));
            } else {
                counts.put(curr, i);
            }
        }
        return ans;
    }
}
