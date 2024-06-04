class Solution {
    public String reversePrefix(String word, char ch) {
        //look for ch && reverse? and then return
        char[] curr = word.toCharArray();
        int pointer = 0;
        while(curr[pointer] != ch && pointer < word.length() - 1) {
            pointer++;
        }
        if (pointer == word.length() - 1 && curr[pointer] != ch) {
            return String.valueOf(curr);
        }

        int left = 0;
        while(left < pointer) {
            char temp = curr[left];
            curr[left] = curr[pointer];
            curr[pointer] = temp;
            left++;
            pointer--;
        }
       return String.valueOf(curr); 
    }
}
