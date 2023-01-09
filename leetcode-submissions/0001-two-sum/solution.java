class Solution {

    //O(n^2) solution
    // public int[] twoSum(int[] nums, int target) {
    //     for (int i = 0; i < nums.length - 1; i++) {
    //         for (int j = i + 1; j < nums.length; j++) {
    //             if (nums[i] + nums[j] == target) {
    //                 int[] arr = new int[2];
    //                 arr[0] = i;
    //                 arr[1] = j;
    //                 return arr;
    //             }

    //         }
    //     }
    //     return null;
    // }

    //this is in o(n) + o(nlgn) for sorting -- but with this we loose the index of the integers 
    // since we are sorting them
    // public int[] twoSum(int[] nums, int target) {
    //     Arrays.sort(nums);
    //     int lo = 0; int hi = nums.length - 1;
    //     int[] ans = new int[2];

    //     while (lo < hi) {
    //         int sum  = nums[lo] + nums[hi];
    //         // System.out.println("curr");
    //         // System.out.println(lo);
    //         // System.out.println(hi);
    //         // System.out.println(sum);
    //         if (sum < target) {
    //             lo++;
    //         } else if (sum > target) {
    //             hi--;
    //         } else {
    //             ans[0] = lo;
    //             ans[1] = hi;
    //             return ans;
    //         }
    //     }
    //     return ans;
    // }

    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numIndex = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            numIndex.put(nums[i], i);
        }
        for (int j = 0; j < nums.length; j++) {
            int subs = target - nums[j];
            if (numIndex.containsKey(subs) && numIndex.get(subs) != j) {
                return new int[] {j, numIndex.get(subs)};
            }
        }
        return null;
    }


}
