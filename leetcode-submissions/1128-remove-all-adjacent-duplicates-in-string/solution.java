class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> stack = new Stack<>();
        char[] chars = s.toCharArray();
        stack.push(chars[0]);
        for(int i = 1; i < chars.length; i++) {
            if (!stack.isEmpty() && stack.peek() == chars[i]) {
                stack.pop();
            } else {
                stack.push(chars[i]);
            }
        }

        String ans = "";
        while(!stack.isEmpty()) {
            ans = stack.pop() + ans;
        }
        return ans;    
    }
}
