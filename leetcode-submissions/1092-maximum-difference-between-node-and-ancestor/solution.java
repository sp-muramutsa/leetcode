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
    public int maxAncestorDiff(TreeNode root) {
        return getMaxMin(root, root.val, root.val);
    }
    
    public int getMaxMin(TreeNode curr, int max, int min) {
        if (curr == null) {
            return max - min;
        }
        max = Math.max(max, curr.val);
        min = Math.min(min, curr.val);
        int right = getMaxMin(curr.right, max, min);
        int left = getMaxMin(curr.left, max, min);
        return Math.max(right, left);
    }
}
