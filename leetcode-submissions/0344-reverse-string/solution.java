class Solution {
    public void reverseString(char[] s) {
        //aced...
        int forward = 0;
        int backward = s.length - 1;
        while(forward < backward) {
            char temp = s[backward];
            s[backward] = s[forward];
            s[forward] = temp;
            forward++;
            backward--;
        } 
    }
}
