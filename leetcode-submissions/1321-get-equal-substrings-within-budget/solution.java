class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        /**
            looking for a substring not exceeding maxCost...
            the rest of the things can be viewed as a difference between two numbers
         */

        int ans = 0;
        int left = 0;
        int currCost = 0;
        for(int right = 0; right < s.length(); right++) {
            currCost += Math.abs(s.charAt(right) - t.charAt(right));
            while(currCost > maxCost) {
                currCost -= Math.abs(s.charAt(left) - t.charAt(left));
                left++;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
