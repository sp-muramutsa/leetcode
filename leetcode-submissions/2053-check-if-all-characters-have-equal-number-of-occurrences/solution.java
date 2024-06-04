class Solution {
    public boolean areOccurrencesEqual(String s) {
        //store occurences and check if its the same number
        Map<Character, Integer> curr = new HashMap<>();
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            curr.put(c, curr.getOrDefault(c, 0) + 1);
        }
        // Set keys = curr.keySet();
        // int counts = curr.get(keys.iterator().next());
        // for(char key: curr.keySet()) {
        //     if (curr.get(key) != counts) {
        //         return false;
        //     }
        // }
        // return true;
        Set<Integer> freqs = new HashSet<>(curr.values());
        return freqs.size() == 1;
    }
}
