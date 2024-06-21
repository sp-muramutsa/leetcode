/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int getDecimalValue(ListNode head) {
        int size = 0;
        ListNode curr = head;
        while(curr.next != null) {
            size++;
            curr = curr.next;
        }

        int ans = 0;
        ListNode secondLooper = head;
        while(secondLooper != null) {
            if (secondLooper.val == 1) {
                ans += Math.pow(2, size);
            }
            secondLooper = secondLooper.next;
            size--;
        }
        return ans;
    }
}
