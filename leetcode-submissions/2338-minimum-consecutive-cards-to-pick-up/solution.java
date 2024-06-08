class Solution {
    public int minimumCardPickup(int[] cards) {
        /**
        map nums[i] -- i 
        and keep recording the min
         */

        int ans = Integer.MAX_VALUE;
        Map<Integer, Integer> freq = new HashMap<>();
        for(int i = 0; i < cards.length; i++) {
            int card = cards[i];
            if (freq.containsKey(card)) {
                ans = Math.min(ans, i - freq.get(card) + 1);
                freq.put(card, i);
            } else {
                freq.put(card, i);
            }
        }
        if (ans == Integer.MAX_VALUE) {
            ans = -1;
        }
        return ans;
    }
}
