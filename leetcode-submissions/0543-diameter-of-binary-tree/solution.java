/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int ans;
    public int diameterOfBinaryTree(TreeNode root) {
        ans = 0;
        helper(root);
        return ans;
    }

    private int helper(TreeNode node) {
        if (node == null) {return 0;}
        int right =  helper(node.right);
        int left = helper(node.left);
        ans = Math.max(ans, left + right);
        return Math.max(right, left) + 1;
    }
}
