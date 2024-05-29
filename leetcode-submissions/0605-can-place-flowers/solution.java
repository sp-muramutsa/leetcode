class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        //check before and after
        //3, check before, update n, and update flowerbed

        //edge cases...
        if (n == 0) { return true; }
        for (int i = 0; i < flowerbed.length ; i++) {
            if (
                (i == 0 || flowerbed[i-1] == 0) &&
                flowerbed[i] == 0 &&
                (i == flowerbed.length - 1 || flowerbed[i+1] == 0)
            ) {
                flowerbed[i] = 1;
                n--;
                if (n == 0) {
                    return true;
                }
            }
        }
        return false; 
    }
}
