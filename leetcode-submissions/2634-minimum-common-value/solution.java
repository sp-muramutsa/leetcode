class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        //0(n + m)
        int left = 0;
        int right = 0;
        while(left < nums1.length && right < nums2.length) {
            if (nums2[right] < nums1[left]) {
                right++;
            } else if (nums2[right] > nums1[left]) {
                left++;
            } else {
                return nums1[left];
            }
        }
        return -1;
    }
}
