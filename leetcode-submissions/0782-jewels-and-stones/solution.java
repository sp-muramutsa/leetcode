class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        //jewels in a hashset, and then go through stones counting
        
        Set<Character> chars = new HashSet<>();
        for(char c: jewels.toCharArray()) {
            chars.add(c);
        }
        
        int ans = 0;
        for(char ch: stones.toCharArray()) {
            if (chars.contains(ch)) {
                ans++;
            }
        }
        return ans;
    }
}
