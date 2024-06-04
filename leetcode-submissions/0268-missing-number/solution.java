class Solution {
    public int missingNumber(int[] nums) {
        Set<Integer> numSet = new HashSet<Integer>();
        for(int i = 0; i <= nums.length; i++) {
            numSet.add(i);
        }
        for(int num: nums) {
            numSet.remove(num);
        }
        return numSet.iterator().next();
        
    }
}
