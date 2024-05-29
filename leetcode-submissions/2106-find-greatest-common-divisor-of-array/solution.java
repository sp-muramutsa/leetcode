class Solution {
    public int findGCD(int[] nums) {
        int smallest = nums[0];
        int biggest = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < smallest) {
                smallest = nums[i];
            }
            if (nums[i] > biggest) {
                biggest = nums[i];
            }
        }
        return gcd(biggest, smallest);
        
    }

    private int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a%b);
        }
    }
}
