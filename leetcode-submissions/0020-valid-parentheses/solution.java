class Solution {
    public boolean isValid(String s) {
        char[] chars = s.toCharArray();
        Stack<Character> a = new Stack<Character>();
        for(char c: chars) {
            if (c == '(') {
                a.push(')');
            } else if (c == '{') {
                a.push('}');
            } else if (c == '[') {
                a.push(']');
            } else if (a.isEmpty() || a.pop() != c){
                return false;
            }
        }
        return a.isEmpty();
    }

    //     public boolean isValid(String s) {
    //     char[] chars = s.toCharArray();
    //     Stack<Integer> a = new Stack<Integer>();
    //     Stack<Integer> b = new Stack<Integer>();
    //     Stack<Integer> d = new Stack<Integer>();

    //     for(char c: chars) {
    //         if (c == '(') {
    //             a.push(1);
    //         } else if (c == ')') {
    //             if(a.isEmpty()) { return false;}
    //             a.pop();
    //         } else if (c == '{') {
    //             b.push(1);
    //         } else if (c == '}') {
    //             if(b.isEmpty()) { return false;}
    //             b.pop();
    //         } else if (c == '[') {
    //             d.push(1);
    //         } else if (c == ']') {
    //             if(d.isEmpty()) { return false;}
    //             d.pop();
    //         } else {
    //             return false;
    //         }
    //     }
    //     return a.isEmpty() && b.isEmpty() && d.isEmpty();
    // }
}
