class Solution {
    public String makeGood(String s) {
        //if curr is a uppercase of the stack top... don't append it
        //stringbuilder.. 
        StringBuilder sb = new StringBuilder();
        for(int i= 0; i < s.length(); i++) {
            if (!sb.isEmpty() && Math.abs(s.charAt(i) - sb.charAt(sb.length() - 1)) == 32) {
                sb.deleteCharAt(sb.length() - 1);
            } else {
                sb.append(s.charAt(i));
            }
        }
        return sb.toString();
    }
}
