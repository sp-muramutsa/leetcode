class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < word1.length() && i < word2.length(); i++) {
            sb.append(word1.charAt(i));
            sb.append(word2.charAt(i));
        }
        
        if (word1.length() > word2.length()) {
            sb.append(word1.substring(word2.length()));
        } else {
            sb.append(word2.substring(word1.length()));
        }
        return sb.toString();
    }
}
