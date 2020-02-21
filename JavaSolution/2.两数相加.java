/*
 * @lc app=leetcode.cn id=2 lang=java
 *
 * [2] 两数相加
 *
 * https://leetcode-cn.com/problems/add-two-numbers/description/
 *
 * algorithms
 * Medium (36.33%)
 * Likes:    3701
 * Dislikes: 0
 * Total Accepted:    295.4K
 * Total Submissions: 813.1K
 * Testcase Example:  '[2,4,3]\n[5,6,4]'
 *
 * 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
 * 
 * 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
 * 
 * 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
 * 
 * 示例：
 * 
 * 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
 * 输出：7 -> 0 -> 8
 * 原因：342 + 465 = 807
 * 
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list. 
 * public class ListNode 
 * { int val; 
 * ListNode next; 
 * ListNode(int x) { val = x; } }
 */

 // T:O(max(m,n)) S:O(max(m,n))
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode p = l1, q = l2, curr = dummyHead;
        int carry = 0;
        while (p != null || q != null) {
            int x = (p != null) ? p.val : 0;
            int y = (q != null) ? q.val : 0;
            int sum = carry + x + y;
            carry = sum / 10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;
            if (p != null)
                p = p.next;
            if (q != null)
                q = q.next;
        }
        if (carry > 0) {
            curr.next = new ListNode(carry);
        }
        return dummyHead.next;
    }
}

class Main {
    public static void main(String[] args) {
        // Create a new Solution instance
        Solution solution = new Solution();
        // Create a test case
        ListNode l1 = buildTestListNode(new int[] { 2, 4, 3 });
        ListNode l2 = buildTestListNode(new int[] { 5, 6, 4 });
        // Get the answer
        ListNode answer = solution.addTwoNumbers(l1, l2);
        // Print the answer
        System.out.println(answer.toString());
    }

    // 尾插法构建List
    public static ListNode buildTestListNode(int[] nums) {
        ListNode res = new ListNode(0);
        if (nums == null || nums.length <= 0) {
            return res;
        }
        ListNode tailer;
        tailer = res = null;
        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                tailer = res = new ListNode(nums[i]);
            } else {
                ListNode temp = new ListNode(nums[i]);
                tailer.next = temp;
                tailer = temp;
            }
        }
        return res;
    }
}
// @lc code=end
