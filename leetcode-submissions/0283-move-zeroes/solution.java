// class Solution {
//     public void moveZeroes(int[] nums) {
//         for(int i = 0; i < nums.length; i++) {
//             if (nums[i] == 0) {
//                 int j = i + 1;
//                 while(j < nums.length) {
//                     if (nums[j] != 0) {
//                         int temp = nums[i];
//                         nums[i] = nums[j];
//                         nums[j] = temp;
//                         break;
//                     }
//                     j++;
//                 }
//             }
//         }
//     }
// }

class Solution {
    public void moveZeroes(int[] nums) {
        //two pointer... one checking for zero other for nonzero and keep switching
        //?sliding window? where left is stays with zeroes and right looks for the next nonzero

        int l = 0;
        while(nums[l] != 0 && l < nums.length - 1) {
            l++;
        }
        boolean foundZero = nums[l] == 0;
        for(int r = l; r < nums.length; r++) {
            if(nums[r] != 0 && foundZero) {
                nums[l] = nums[r];
                nums[r] = 0;
                while(nums[l] != 0) {
                    l++;
                }
                foundZero = nums[l] == 0;
            }
        }
    }
}
