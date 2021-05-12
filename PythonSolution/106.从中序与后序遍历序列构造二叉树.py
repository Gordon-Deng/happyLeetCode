#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (71.77%)
# Likes:    498
# Dislikes: 0
# Total Accepted:    106.2K
# Total Submissions: 147.9K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# 根据一棵树的中序遍历与后序遍历构造二叉树。
# 
# 注意:
# 你可以假设树中没有重复的元素。
# 
# 例如，给出
# 
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 
# 返回如下的二叉树：
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def dfs(inorder, i_start, i_end, postorder, p_start, p_end):
            if i_start > i_end: return None
            if i_start == i_end: return TreeNode(inorder[i_start])
            node = TreeNode(postorder[p_end])
            i = inorder.index(postorder[p_end])
            node.left = dfs(inorder, i_start, i - 1, postorder, p_start, p_start + (i - 1 - i_start))
            node.right = dfs(inorder, i + 1, i_end, postorder, p_start + (i - 1 - i_start) + 1, p_end - 1)
            return node
        return dfs(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)
# @lc code=end

