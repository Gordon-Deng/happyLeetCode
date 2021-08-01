#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
# https://leetcode-cn.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (64.92%)
# Likes:    507
# Dislikes: 0
# Total Accepted:    124.2K
# Total Submissions: 191K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
# 
# 
# 示例 2:
# 
# 
# 输入: [1,null,3]
# 输出: [1,3]
# 
# 
# 示例 3:
# 
# 
# 输入: []
# 输出: []
# 
# 
# 
# 
# 提示:
# 
# 
# 二叉树的节点个数的范围是 [0,100]
# -100  
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
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        depth_flag = dict()
        max_dapth = -1

        stack = [(root, 0)]
        while stack :
            node, depth = stack.pop()

            if node is not None :
                max_dapth = max(max_dapth, depth)

                # setdefault新方法
                depth_flag.setdefault(depth, node.val)
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
                
        return [depth_flag[index] for index in range(max_dapth+1)]
# @lc code=end

