#
# @lc app=leetcode.cn id=1038 lang=python3
#
# [1038] 把二叉搜索树转换为累加树
#
# https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/description/
#
# algorithms
# Medium (78.37%)
# Likes:    111
# Dislikes: 0
# Total Accepted:    20.4K
# Total Submissions: 25.8K
# Testcase Example:  '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'
#
# 给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node
# 的新值等于原树中大于或等于 node.val 的值之和。
# 
# 提醒一下，二叉搜索树满足下列约束条件：
# 
# 
# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。
# 
# 
# 注意：该题目与 538: https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
# 相同
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# 
# 
# 示例 2：
# 
# 输入：root = [0,null,1]
# 输出：[1,null,1]
# 
# 
# 示例 3：
# 
# 输入：root = [1,0,2]
# 输出：[3,3,2]
# 
# 
# 示例 4：
# 
# 输入：root = [3,2,4,1]
# 输出：[7,9,4,10]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数介于 1 和 100 之间。
# 每个节点的值介于 0 和 100 之间。
# 树中的所有值 互不相同 。
# 给定的树为二叉搜索树。
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right#

# 方法一：反中序遍历即可
# T:O(N)) S:O(N)
# class Solution:
#     def bstToGst(self, root: TreeNode) -> TreeNode:
#         def dfs(root : TreeNode):
#             nonlocal total
#             if root:
#                 dfs(root.right)
#                 total += root.val
#                 root.val = total
#                 dfs(root.left)
        
#         total = 0
#         dfs(root)
#         return root

# 技巧题
# 方法二：Morris 遍历（最优）
#1.如果当前节点的右子节点为空，处理当前节点，并遍历当前节点的左子节点；

#2.如果当前节点的右子节点不为空，找到当前节点右子树的最左节点（该节点为当前节点中序遍历的前驱节点）；
#  * 如果最左节点的左指针为空，将最左节点的左指针指向当前节点，遍历当前节点的右子节点；
#  * 如果最左节点的左指针不为空，将最左节点的左指针重新置为空（恢复树的原状），处理当前节点，并将当前节点置为其左节点；
#3.重复步骤 1 和步骤 2，直到遍历结束。
# T:O(N) S:O(1)
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def getSuccessor(node: TreeNode) -> TreeNode:
            succ = node.right
            while succ.left and succ.left != node:
                succ = succ.left
            return succ
        
        total = 0
        node = root

        while node:
            if not node.right:
                total += node.val
                node.val = total
                node = node.left
            else:
                succ = getSuccessor(node)
                if not succ.left:
                    succ.left = node
                    node = node.right
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left

        return root
# @lc code=end

