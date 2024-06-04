class Solution {
    public List<Integer> intersection(int[][] nums) {
        //fill out a map.... if something is the number of arrays... add to sol and sort

        Map<Integer, Integer> map = new HashMap<>();
        for(int[] arr: nums) {
            for(int curr: arr) {
                map.put(curr, map.getOrDefault(curr, 0) + 1);
            }
        }

        List<Integer> ans = new ArrayList<>();
        for(int key: map.keySet()) {
            if (map.get(key) == nums.length) {
                ans.add(key);
            }
        }
        Collections.sort(ans);
        return ans;
    }
}
