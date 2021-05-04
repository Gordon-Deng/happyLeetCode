#
# @lc app=leetcode.cn id=1008 lang=python3
#
# [1008] 前序遍历构造二叉搜索树
#
# https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
#
# algorithms
# Medium (72.85%)
# Likes:    142
# Dislikes: 0
# Total Accepted:    13.5K
# Total Submissions: 18.6K
# Testcase Example:  '[8,5,1,7,10,12]'
#
# 返回与给定前序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。
# 
# (回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，对于 node.left 的任何后代，值总 < node.val，而 node.right
# 的任何后代，值总 > node.val。此外，前序遍历首先显示节点 node 的值，然后遍历 node.left，接着遍历 node.right。）
# 
# 题目保证，对于给定的测试用例，总能找到满足要求的二叉搜索树。
# 
# 
# 
# 示例：
# 
# 输入：[8,5,1,7,10,12]
# 输出：[8,5,10,1,7,null,12]
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= preorder.length <= 100
# 1 <= preorder[i] <= 10^8
# preorder 中的值互不相同
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
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        s, p = [], preorder and [(0, len(preorder), -1)]
        while p:
            l, r, f = p.pop()
            if l < r:
                s.append(TreeNode(preorder[l]))
                if f >= 0:
                    if s[-1].val < s[f].val:
                        s[f].left = s[-1]
                    else:
                        s[f].right = s[-1]
                devide = next((i for i in range(l + 1, r) if preorder[i] > s[-1].val), r)
                p.append((devide, r, l))
                p.append((l + 1, devide, l))
        return s and s[0]
# @lc code=end

