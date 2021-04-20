#
# @lc app=leetcode.cn id=1315 lang=python3
#
# [1315] 祖父节点值为偶数的节点和
#
# https://leetcode-cn.com/problems/sum-of-nodes-with-even-valued-grandparent/description/
#
# algorithms
# Medium (81.03%)
# Likes:    51
# Dislikes: 0
# Total Accepted:    10.8K
# Total Submissions: 13.4K
# Testcase Example:  '[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]'
#
# 给你一棵二叉树，请你返回满足以下条件的所有节点的值之和：
# 
# 
# 该节点的祖父节点的值为偶数。（一个节点的祖父节点是指该节点的父节点的父节点。）
# 
# 
# 如果不存在祖父节点值为偶数的节点，那么返回 0 。
# 
# 
# 
# 示例：
# 
# 
# 
# 输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# 输出：18
# 解释：图中红色节点的祖父节点的值为偶数，蓝色节点为这些红色节点的祖父节点。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目在 1 到 10^4 之间。
# 每个节点的值在 1 到 100 之间。
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# T:O(N) S:O(H)
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        def dfs(gp_val, p_val, node) :
            if not node:
                return
            if gp_val % 2 == 0:
                nonlocal res
                res += node.val
            dfs(p_val, node.val, node.left)
            dfs(p_val, node.val, node.right)

        dfs(1, 1, root)
        return res
        
# @lc code=end

