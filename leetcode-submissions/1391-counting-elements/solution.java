class Solution {
    public int countElements(int[] arr) {
        //create a set, and then check contains?
        //two loops?
        int ans = 0;
        Set<Integer> nums = new HashSet<>();
        for(int i = 0; i < arr.length; i++) {
            nums.add(arr[i]);
        }
        for(int i = 0; i < arr.length; i++) {
            if(nums.contains(arr[i] + 1)) {
                ans++;
            }
        }
        return ans;
    }
}
