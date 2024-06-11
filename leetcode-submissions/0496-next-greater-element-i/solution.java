class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        //just store the a next greater for each element in nums2... 
        
        //stack, if the next number is smaller add to stack
        //if it is greater, keep on popping off of the stack and adding in a hashmap

        Stack<Integer> stack = new Stack<>();
        Map<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < nums2.length; i++) {
            while(!stack.empty() && nums2[i] > stack.peek()) {
                map.put(stack.pop(), nums2[i]);
            }
            stack.push(nums2[i]);
        }
        
        int[] ans = new int[nums1.length];
        for(int k = 0; k <nums1.length; k++) {
            ans[k] = map.getOrDefault(nums1[k], -1);
        }
        return ans;   
    }
}
