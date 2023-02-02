

class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        Map<Integer, Integer> frequencies = new HashMap();
        for (int i = 0; i < nums.length; i++) {
            frequencies.put(nums[i], frequencies.getOrDefault(nums[i], 0) + 1);
        }

        Queue<Integer> heap = new PriorityQueue<>((n1, n2) -> frequencies.get(n1) - frequencies.get(n2));
        for (int key: frequencies.keySet()) {
            heap.add(key);

            if (heap.size() > k) {
                heap.poll();
            }
        }

        int[] ans = new int[k];
        for (int i = 0; i < k; i++) {
            ans[i] = heap.poll();
        }
        return ans;
    }
}
