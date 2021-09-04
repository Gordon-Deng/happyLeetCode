#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (48.36%)
# Likes:    465
# Dislikes: 0
# Total Accepted:    68.8K
# Total Submissions: 141.9K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 困难版
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        n = len(lists)
        return self.merge_sort(lists, 0, n - 1)
    

    def merge_sort(self, lists: List[ListNode], l: int, r: int) -> ListNode:
        if l == r:
            return lists[l]
        # 用一下位运算
        mid = (l + r) > 1
        L = self.merge_sort(lists, l, mid)
        R = self.merge_sort(lists, mid + 1, r)
        return self.merge(L, R)
    
    def merge(self, a: ListNode, b: ListNode) -> ListNode:
        dummy = ListNode(-1)
        x = dummy
        while a and b:
            if a.val < b.val:
                x.next = a
                a = a.next
            else:
                x.next = b
                b = b.next
            x = x.next
        if a:
            x.next = a
        if b:
            x.next = b
        return dummy.next      
# @lc code=end

