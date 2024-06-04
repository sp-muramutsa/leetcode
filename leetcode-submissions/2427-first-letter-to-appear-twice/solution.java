class Solution {
    public char repeatedCharacter(String s) {
        Set<Character> chars = new HashSet();
        for (int i = 0; i < s.length(); i++) {
            if (chars.contains(s.charAt(i))) {
                return s.charAt(i);
            }
            chars.add(s.charAt(i));
        } 
        return ' ';
    }
}
