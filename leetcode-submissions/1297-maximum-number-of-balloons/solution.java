class Solution {
    public int maxNumberOfBalloons(String text) {
        /**
        parse through and only store the occurence of b a n l o 
        compare the counts
        */
        
        Map<Character, Integer> counts = new HashMap<>();
        for(int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (isInBalloon(c)) {
                counts.put(c, counts.getOrDefault(c, 0) + 1);
            }
        }
        
        if(counts.get('b') == null || counts.get('a') == null || counts.get('l') == null ||                counts.get('o') == null || counts.get('n') == null) {
            return 0;
        }
        
        counts.put('l', counts.get('l')/2);
        counts.put('o', counts.get('o')/2);
        
        int ans = Integer.MAX_VALUE;
        for(char a: counts.keySet()) {
            if (ans > counts.get(a)) {
                ans = counts.get(a);
            }
        }
        return ans;
    }
    
    private boolean isInBalloon(char c) {
        return c == 'b' || c == 'a' || c == 'n' || c == 'l' || c == 'o' || 
            c == 'B' || c == 'A' || c == 'N' || c == 'L' || c == 'O';
    }
}
