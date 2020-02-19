/*
 * @lc app=leetcode.cn id=21 lang=cpp
 *
 * [21] 合并两个有序链表
 *
 * https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
 *
 * algorithms
 * Easy (59.03%)
 * Likes:    856
 * Dislikes: 0
 * Total Accepted:    184.1K
 * Total Submissions: 308.2K
 * Testcase Example:  '[1,2,4]\n[1,3,4]'
 *
 * 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
 * 
 * 示例：
 * 
 * 输入：1->2->4, 1->3->4
 * 输出：1->1->2->3->4->4
 * 
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// T:O(n+m) S:O(1)
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        //很巧妙地引入一个特殊结点preHead
        ListNode* preHead = new ListNode(-1);
        ListNode* pre = preHead;
        //循环直到至少有一个链表到末尾后才结束
        while(l1 && l2) {
            //l1、l2中结点的较小者拼接在以preHead->next为头结点的结果链表后面
            if(l1->val >= l2->val) {
                pre->next = l2;
                l2 = l2->next;
            }
            else {
                pre->next = l1;
                l1 = l1->next;
            }
            pre = pre->next;
        }
        pre->next =  l1==NULL ? l2 : l1;
        return preHead->next;
    }
};
// @lc code=end

