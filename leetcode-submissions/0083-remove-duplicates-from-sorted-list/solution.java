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
    public ListNode deleteDuplicates(ListNode head) {
        //set
        Set<Integer> vals = new HashSet<>();
        
        if (head == null || head.next == null) {
            return head;
        }
        ListNode prev = head;
        ListNode curr = head.next;
        vals.add(prev.val);
        while(curr != null) {
            int val = curr.val;
            if (vals.contains(val)) {
                prev.next = curr.next;
                curr = curr.next;
            } else {
                vals.add(val);
                prev = curr;
                curr = curr.next;
            } 
        }
        // 1, 2, 1, 4, 2
        //set = 1, 2, 4,
        return head;  
    }
}
