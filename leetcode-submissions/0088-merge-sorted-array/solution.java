class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {

        int k1 = m - 1;
        int k2 = n - 1;
        int k3 = m + n - 1;

        while (k3 >= 0) {
            if (k2 < 0) {
                return;
            }
            if (k1 >= 0 && nums1[k1] >= nums2[k2]) {
                nums1[k3] = nums1[k1];
                k1--;
            } else {
                nums1[k3] = nums2[k2];
                k2--;
            }
            k3--;
        } 
    }
}
