#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#
# https://leetcode-cn.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (72.65%)
# Likes:    169
# Dislikes: 0
# Total Accepted:    36K
# Total Submissions: 49.5K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，在树的最后一行找到最左边的值。
# 
# 示例 1:
# 
# 
# 输入:
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# 输出:
# 1
# 
# 
# 
# 
# 示例 2: 
# 
# 
# 输入:
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   5   6
# ⁠      /
# ⁠     7
# 
# 输出:
# 7
# 
# 
# 
# 
# 注意: 您可以假设树（即给定的根节点）不为 NULL。
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS,先放右边的节点
# DFS因为要加level的判断，所以反而没有BFS巧妙
# T:O(N) S:O(WIDHT)
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            # 先右后左
            if node.right: 
                queue.append(node.right)
            if node. left:
                queue.append(node.left)
        return node.val
# @lc code=end

