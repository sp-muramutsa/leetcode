class Solution {
    public int[] sortedSquares(int[] nums) {
        //it's basically sorted but in two different directions
        int smallestLoc = 0;
        int smallest = Integer.MAX_VALUE;
        for(int i = 0; i < nums.length; i++) {
            if (Math.abs(nums[i]) < smallest) {
                smallestLoc = i;
                smallest = Math.abs(nums[i]);
            }
            nums[i] = nums[i] * nums[i];
        } //0(n)
        
        int[] ans = new int[nums.length];
        int left = smallestLoc - 1;
        int right = smallestLoc;
        int pointer = 0;
        while(left >= 0 && right < nums.length) {
            if(nums[left] < nums[right]) {
                ans[pointer] = nums[left];
                left--;
            } else {
                ans[pointer] = nums[right];
                right++;
            }
            pointer++;
        }
        
        while (left >= 0) {
            ans[pointer] = nums[left];
            left--;
            pointer++;
        }
        
        while (right < nums.length) {
            ans[pointer] = nums[right];
            right++;
            pointer++;
        }
        return ans;
        
    }
}
