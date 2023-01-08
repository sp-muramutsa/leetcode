class Solution {
    public String longestCommonPrefix(String[] strs) {
        String ans = strs[0];
        for (int i = 1; i < strs.length; i++) {
            ans = longestCommonPrefixBetweenTwostrings(ans, strs[i]);
            if (ans == "") return ans;
        }
        return ans;
    }

    public String longestCommonPrefixBetweenTwostrings(String a, String b) {
        char[] aChars = a.toCharArray();
        char[] bChars = b.toCharArray();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < aChars.length && i < bChars.length; i++)  {
            if (aChars[i] != bChars[i]) {
                return sb.toString();
            } else {
                sb.append(aChars[i]);
            }
        }
        return sb.toString();
    }
}
