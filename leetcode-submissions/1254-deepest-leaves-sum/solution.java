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
    public int deepestLeavesSum(TreeNode root) {
        int currAns = 0;
        Queue<TreeNode> row = new LinkedList<>();
        row.add(root);
        while(!row.isEmpty()) {
            int size = row.size();
            currAns = 0;
            for(int i =0; i < size; i++) {
                TreeNode curr = row.remove();
                currAns += curr.val;
                if (curr.right != null) { 
                    row.add(curr.right); 
                }
                if (curr.left != null) { 
                    row.add(curr.left); 
                }
            }
        }
        return currAns;  
    }
}
