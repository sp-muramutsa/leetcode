class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        //sort and return? this would have worked if it was just for checking equality
        // char[] ran = ransomNote.toCharArray();
        // Arrays.sort(ran);
        // char[] mag = magazine.toCharArray();
        // Arrays.sort(mag);
        // return String.valueOf(ran).equals(String.valueOf(mag)); 
        
        //26 keys max
        //fill it up with magazine frequencies
        //and subtract for ransomNote frequencies.
        
        Map<Character, Integer> freq = new HashMap<>();
        for(char c: magazine.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
                
        for(char ch: ransomNote.toCharArray()) {
            if (freq.containsKey(ch) && freq.get(ch) > 0) {
                freq.put(ch, freq.get(ch) - 1);
            } else {
                return false;
            }
        }
        return true; 
    }
}
