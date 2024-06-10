class Solution {
    public String simplifyPath(String path) {
        /**
        get substring? split by /
        a stack of substrings
         */
        String[] splits = path.split("\\/");
        Stack<String> stack = new Stack<>();
        for(String s: splits) {
            if (!stack.isEmpty() && s.equals("..")) {
                stack.pop();
            } else if (!s.equals(".") && !s.equals("") && !s.equals("..")) {
                stack.push(s);
            }
        }

        String sb = "";
        while(!stack.isEmpty()) {
            sb = "/" + stack.pop() + sb;
        }

        if (sb.isEmpty()) {
            return "/";
        }

        return sb;
    }
}
