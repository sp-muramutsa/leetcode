class Solution {
    public String reverseWords(String s) {
        //charArray and two pointer
        String[] sArr = s.split("\\s+");
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < sArr.length; i++) {
            char[] curr = sArr[i].toCharArray();
            int left = 0;
            int right = curr.length - 1;
            while(left < right) {
                char temp = curr[left];
                curr[left] = curr[right];
                curr[right] = temp;
                left++;
                right--;
            }
            sArr[i] = String.valueOf(curr);

            if (i < sArr.length - 1) {
                sb.append(sArr[i]);
                sb.append(" ");
            }
        }
        sb.append(sArr[sArr.length - 1]);
        return sb.toString();   
    }
}
