class Solution {
    public int maximumSum(int[] nums) {
        /**
            Sum of digits will be from 0 --> 10
            Create a map with keys 0 -> 10
            
            get max sum -- sort and add last two -- 0 nlgn
            better? in 0 n
         */

        // Map<Integer, List<Integer>> freq = new HashMap<>();
        // for(int num: nums) {
        //     int sum = 0;
        //     int numDup = num;
        //     while(num > 0) {
        //         sum += num % 10;
        //         num /= 10;
        //     }
        //     if(!freq.containsKey(sum)) {
        //         freq.put(sum, new ArrayList<>());
        //     }
        //     freq.get(sum).add(numDup);
        // }
        // int largestSum = -1;
        // for(int key: freq.keySet()) {
        //     List<Integer> val = freq.get(key);
        //     if (val.size() > 1) {
        //         Collections.sort(val, Collections.reverseOrder());
        //         largestSum = Math.max(largestSum, val.get(0) + val.get(1));
        //     }
        // } 
        // return largestSum;

        Map<Integer, Integer> freq = new HashMap<>();
        int largestSum = -1;
        for(int num: nums) {
            int sum = 0;
            int numDup = num;
            while(numDup > 0) {
                sum += numDup % 10;
                numDup /= 10;
            }
            if(freq.containsKey(sum)) {
                int val = freq.get(sum);
                largestSum = Math.max(largestSum, val + num);
                freq.put(sum, Math.max(val, num));
            } else {
                freq.put(sum, num);
            }
        }
        return largestSum;
    }
}
