#
# @lc app=leetcode.cn id=1302 lang=python3
#
# [1302] 层数最深叶子节点的和
#
# https://leetcode-cn.com/problems/deepest-leaves-sum/description/
#
# algorithms
# Medium (81.28%)
# Likes:    48
# Dislikes: 0
# Total Accepted:    15.3K
# Total Submissions: 18.8K
# Testcase Example:  '[1,2,3,4,5,null,6,7,null,null,null,null,8]'
#
# 给你一棵二叉树的根节点 root ，请你返回 层数最深的叶子节点的和 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# 输出：15
# 
# 
# 示例 2：
# 
# 
# 输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# 输出：19
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [1, 10^4] 之间。
# 1 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# T:O(N) S:O(N)
# class Solution:
#     def deepestLeavesSum(self, root: TreeNode) -> int:
#         q = collections.deque([(root, 0)])
#         maxdep, total = -1, 0
#         while len(q) > 0:
#             node, dep = q.pop()
#             if dep > maxdep:
#                 maxdep, total = dep, node.val
#             elif dep == maxdep:
#                 total += node.val
#             if node.left:
#                 q.append((node.left, dep + 1))
#             if node.right:
#                 q.append((node.right, dep + 1))
#         return total


# collections.deque([(root, 0)]) 里面的[(root, 0)]就是简单的往列表中塞了一个元组，因为后面pop的时候是出两个值
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = collections.deque([(root, 0)])
        maxdep, total = -1, 0
        while len(q) > 0:
            node, dep = q.pop()
            if dep > maxdep:
                maxdep, total = dep, node.val
            elif dep == maxdep:
                total += node.val
            if node.left:
                q.append((node.left, dep + 1))
            if node.right:
                q.append((node.right, dep + 1))
        return total
# @lc code=end

