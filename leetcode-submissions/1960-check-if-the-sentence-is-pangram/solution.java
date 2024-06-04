class Solution {
    public boolean checkIfPangram(String sentence) {
        //set and check if the size is 26?
        
        Set<Character> chars = new HashSet<>();
        for(int i = 0; i < sentence.length(); i++) {
            chars.add(sentence.charAt(i));
        }
        return chars.size() == 26;
        
    }
}
