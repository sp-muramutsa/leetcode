class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int largestNumber = 0;
        for (int i = 0; i < candies.length; i++) {
            if (candies[i] > largestNumber) {
                largestNumber = candies[i];
            }
        }

        List<Boolean> res = new ArrayList<>();

        for (int j = 0; j < candies.length; j++) {
            res.add(candies[j] + extraCandies >= largestNumber);
        }
        return res;
    }
}
