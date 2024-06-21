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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode move = head;
        ListNode lminus1;
        ListNode leftNode;
        ListNode dummy = new ListNode(0, head);
        int counter = 1;
        if (left > 1) {
            while(counter < left - 1) {
                move = move.next;
                counter++;
            }
            lminus1 = move;
            leftNode = move.next;
        } else {
            lminus1 = dummy;
            leftNode = move;
        }

        if(right > 1) {
            while(counter < right && move != null) {
                move = move.next;
                counter++;
            }
        }
        ListNode rightNode = move;

        ListNode prev = rightNode.next;
        while(leftNode != rightNode && leftNode != null) {
            ListNode nextNode = leftNode.next;
            leftNode.next = prev;
            prev = leftNode;
            leftNode = nextNode;
        }
        lminus1.next = rightNode; 
        rightNode.next = prev;
        return dummy.next;
    }
}
