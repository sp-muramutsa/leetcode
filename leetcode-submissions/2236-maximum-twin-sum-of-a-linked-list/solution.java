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
    public int pairSum(ListNode head) {
        /**
        create a reversed version and stop in the middle?
        reverse one part, the second part and then compare them
        */
        ListNode dummy = head;
        ListNode slow = head;
        ListNode fast = head;

        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode prev = null;
        while(slow != null) {
            ListNode nextNode = slow.next;
            slow.next = prev;
            prev = slow;
            slow = nextNode;
        }

        int ans = Integer.MIN_VALUE;

        while(prev != null) {
            ans = Math.max(ans, prev.val + dummy.val);
            dummy = dummy.next;
            prev = prev.next;
        }
        return ans;
    }
}
