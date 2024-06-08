class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        /**
        a sorted str is the key, and the strs are the values.

         */

        Map<String, List<String>> curr = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            String s = strs[i];
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = String.valueOf(chars);
            if (!curr.containsKey(key)) {
                curr.put(key, new ArrayList());
            }
            curr.get(key).add(s);
        }
        return new ArrayList(curr.values());
    }
}
