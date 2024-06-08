class Solution {
    public int equalPairs(int[][] grid) {
        /**
        brute force... get all the row arrays and col arrays... and compare them 0(n^3)
         */
        // int ans = 0;
        // for(int r = 0; r < grid.length; r++) {
        //     for(int c = 0; c < grid.length; c++) {
        //         boolean match = true;
        //         for (int i = 0; i < grid.length; i++) {
        //             if(grid[r][i] != grid[i][c]) {
        //                 match = false;
        //                 break;
        //             }
        //         }
        //         ans += match ? 1 : 0;
        //     }
        // }
        // return ans;

        /**
        HashMap sln
        
        row as a hashobject
         */

        Map<String, Integer> freq = new HashMap<>();
        int n = grid.length;
        int ans = 0;
        for(int i = 0; i < n; i++) {
            String row = Arrays.toString(grid[i]);
            freq.put(row, freq.getOrDefault(row, 0) + 1);
        }

        for(int j = 0; j < n; j++) {
            int[] col = new int[n];
            for (int r = 0; r < n; r++) {
                col[r] = grid[r][j];
            }
            if (freq.containsKey(Arrays.toString(col))) {
                ans += freq.get(Arrays.toString(col));
            }
        }
        return ans;
    }
}
