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
    // public ListNode oddEvenList(ListNode head) {
    //     ListNode dummy = new ListNode(0, head);
    //     ListNode even = head.next;
    //     ListNode prev = head;
    //     while(head != null && head.next != null) {
    //         System.out.println("odd " + head.val);
    //         head.next = head.next.next;
    //         prev = head;
    //         head = head.next;
    //     }

    //     ListNode evenDup = even;
    //     ListNode evenPrev = even;
    //     while(even != null && even.next != null) {

    //         evenPrev = even;
    //         even.next = even.next.next;
    //         even = even.next;
    //     }
    //             // even.next = null;
    //     System.out.println("end " + head.val);
    //     // System.out.println("even " + even.val);
    //     if (even != null) {
    //         even.next = null;
    //     } else {
    //         evenPrev.next = null;
    //     }

    //     if(head != null) {
    //         head.next = evenDup;
    //     } else {
    //         prev = evenDup;
    //     }
    //     return dummy.next;
        
    // }

    //the above didn't work because I moved the pointers for the odd ones and lost even ones.
    public ListNode oddEvenList(ListNode head) {
        if (head == null) {
            return head;
        }
        ListNode dummy = new ListNode(0, head);
        ListNode even = new ListNode(0);
        ListNode currEven = head.next;
        ListNode prevOdd = null;
        while(head != null && head.next != null) {
            ListNode nextNode = head.next;
            head.next = head.next.next;
            prevOdd = head;
            head = head.next;

            even.next = nextNode;
            even = even.next;
        }
        even.next = null;

        if (head != null) {
            head.next = currEven;
        } else {
            prevOdd.next = currEven;
        }
        return dummy.next;
    }
}
