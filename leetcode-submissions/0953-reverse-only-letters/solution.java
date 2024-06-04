class Solution {
    public String reverseOnlyLetters(String s) {
        //two pointers
        int left = 0;
        int right = s.length() - 1;
        char[] curr = s.toCharArray();

        while(left < right) {
            if(Character.isLetter(curr[left]) && Character.isLetter(curr[right])) {
                char temp = curr[left];
                curr[left] = curr[right];
                curr[right] = temp;
                left++;
                right--;
            } else if(Character.isLetter(curr[left])) {
                right--;
            } else {
                left++;
            }
        }
        return String.valueOf(curr);
    }
}
