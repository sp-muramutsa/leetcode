class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> uniques = new HashMap<>();
        char[] chars = s.toCharArray();
        int left = 0;
        int ans = 0;
        for(int right = 0; right < chars.length; right++) {
            char c = chars[right];            
            if(uniques.containsKey(c)) {
                ans = Math.max(ans, right - left); 
                int newLeft = uniques.get(c) + 1;
                while(left < newLeft) { // should update the ones we skipped... sliding window
                    uniques.remove(chars[left]);
                    left++;
                }
            } else {
                ans = Math.max(ans, right - left + 1);
            }
            uniques.put(c, right);
        } 
        return ans;
    }
}
