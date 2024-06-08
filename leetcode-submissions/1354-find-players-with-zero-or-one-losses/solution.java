class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        Set<Integer> win = new HashSet<>();
        Map<Integer, Integer> lose = new HashMap<>();
        for(int[] arr: matches) {
            lose.put(arr[1], lose.getOrDefault(arr[1], 0) + 1);
        }
        for(int[] arr: matches) {
            if(lose.get(arr[0]) == null) {
                win.add(arr[0]);
            }
        }
        List<Integer> oneLoss = new ArrayList<>();
        for(int key: lose.keySet()) {
            if (lose.get(key) == 1) {
                oneLoss.add(key);
            }
        }
        List<Integer> winners = new ArrayList<>(win);
        Collections.sort(oneLoss);
        Collections.sort(winners);
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        ans.add(winners);
        ans.add(oneLoss);
        return ans;
    }
}
