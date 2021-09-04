#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (72.11%)
# Likes:    793
# Dislikes: 0
# Total Accepted:    135.1K
# Total Submissions: 187K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# 给你二叉树的根结点 root ，请你将它展开为一个单链表：
# 
# 
# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,5,3,4,null,6]
# 输出：[1,null,2,null,3,null,4,null,5,null,6]
# 
# 
# 示例 2：
# 
# 
# 输入：root = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [0]
# 输出：[0]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中结点数在范围 [0, 2000] 内
# -100 
# 
# 
# 
# 
# 进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 低端版
# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         preorderList = list()

#         def preorderTraversal(root: TreeNode):
#             if root:
#                 preorderList.append(root)
#                 preorderTraversal(root.left)
#                 preorderTraversal(root.right)
        
#         preorderTraversal(root)
#         size = len(preorderList)
#         for i in range(1, size):
#             prev, curr = preorderList[i - 1], preorderList[i]
#             prev.left = None
#             prev.right = curr

# 高端版
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        root.left, root.right = root.right, root.left

        most_right = root
        while most_right.right:
            most_right = most_right.right

        most_right.right = root.left
        root.left = None
# @lc code=end

