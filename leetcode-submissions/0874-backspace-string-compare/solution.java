class Solution {
    public boolean backspaceCompare(String s, String t) {
        return removeBack(s).equals(removeBack(t));
    }

    public String removeBack(String s) {
        StringBuilder newS = new StringBuilder();
        for(char c: s.toCharArray()) {
            if(c != '#') {
                newS.append(c);
            } else if (newS.length() > 0){
                newS.deleteCharAt(newS.length() - 1);
            }
        }
        return newS.toString();
    }
}
