class Solution {
    public int largestAltitude(int[] gain) {
        //prefixsum... record the highest.. don't need to record the prefixSum array


        int curr = 0;
        int highest = 0;
        for (int i = 0; i < gain.length; i++) {
            curr += gain[i];
            if (curr > highest) {
                highest = curr;
            }
        }
        return highest;
    }
}
