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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int rem = 0;
        ListNode temp;
        ListNode ans = new ListNode(0);
        temp = ans;
        while (l1 != null || l2 != null) {
            int sum;
            if (l1 == null) {
                sum = l2.val + rem;
                l2 = l2.next;
            } else if (l2 == null) {
                sum = l1.val + rem;
                l1 = l1.next; 
            } else {
                sum = l1.val + l2.val + rem;
                l2 = l2.next;
                l1 = l1.next;
            }

            if (sum < 10) {
                rem = 0;
            } else {
                rem = 1;
                sum = sum % 10;
            }
            ans.next = new ListNode(sum);
            ans = ans.next;
        }
        if (rem == 1) {
            ans.next = new ListNode(1);
        }
        return temp.next;
    }
}
