class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < nums.length && nums[i] <=0; i++) {
            if (i == 0 || nums[i - 1] != nums[i]) {
                getList(i, nums, res);
            }
        }
        return res;
    }

    public void getList(int i, int[] nums, List<List<Integer>> res) {

        int lo = i + 1; int hi = nums.length - 1;

        while(lo < hi) {
            int sum = nums[i] + nums[lo] + nums[hi];

            if (sum < 0) {
                lo++;
            } else if (sum > 0) {
                hi--;
            } else {
                res.add(Arrays.asList(nums[i], nums[lo], nums[hi]));
                lo++;
                hi--;
                while (lo < hi && nums[lo] == nums[lo - 1]) {
                    lo++;
                } 
            }
        }
    }

    // public int[] bubbleSort(int[] nums) {
    //     for (int i = 0; i < nums.length - 1; i++) {
    //         for (int j = 0; j < nums.length - i - 1; j++) {
    //             if (nums[j] > nums [j + 1]) {
    //                 int temp = nums [j + 1];
    //                 nums[j + 1] = nums[j];
    //                 nums[j] = temp;
    //             }
    //         }
    //     }
    //     return nums;
    // }
}
