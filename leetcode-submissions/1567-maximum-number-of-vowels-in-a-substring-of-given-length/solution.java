class Solution {
    public int maxVowels(String s, int k) {
        //substring, moving windonw... need to maintain a substring of a certain size
        //keep track of max number of vowels... check for vowels?
        int left = 0;
        int ans = 0;
        int curr = 0;
        if(k > s.length()) { return 0; }
        for(int i = 0; i < k; i++) {
            if (isVowel(s.charAt(i))) {
                curr++;
            }
        }
        ans = Math.max(ans, curr);


        //right, right - i...
        for(int right = k; right < s.length(); right++) {
            if(isVowel(s.charAt(left)) && !isVowel(s.charAt(right))) {
                curr--;
            } else if (!isVowel(s.charAt(left)) && isVowel(s.charAt(right))) {
                curr++;

            }
            left++;
            ans = Math.max(ans, curr);
        }
        return ans;
    }

    private boolean isVowel(char c) { 
        return c == 'i' || c == 'u' || c == 'o' || c == 'a' || c == 'e' ||
                c == 'I' || c == 'U' || c == 'O' || c == 'A' || c == 'E';
    }
}
