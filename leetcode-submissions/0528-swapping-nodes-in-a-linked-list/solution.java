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
    public ListNode swapNodes(ListNode head, int k) {
        ListNode slow = head;
        ListNode fast = head;
        for(int i = 1; i< k; i++) {
            if (fast == null) {
                return null;
            }
            fast = fast.next;
        }
        //at this point fast is at k
        ListNode kth = fast;

        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next;
        }
        //at this point slow is at kth last
        int kLastVal = slow.val;
        slow.val = kth.val;
        kth.val = kLastVal;
        return head;  
    }
}
