#
# @lc app=leetcode.cn id=1448 lang=python3
#
# [1448] 统计二叉树中好节点的数目
#
# https://leetcode-cn.com/problems/count-good-nodes-in-binary-tree/description/
#
# algorithms
# Medium (70.94%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    7.3K
# Total Submissions: 10.3K
# Testcase Example:  '[3,1,4,3,null,1,5]'
#
# 给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。
# 
# 「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：root = [3,1,4,3,null,1,5]
# 输出：4
# 解释：图中蓝色节点为好节点。
# 根节点 (3) 永远是个好节点。
# 节点 4 -> (3,4) 是路径中的最大值。
# 节点 5 -> (3,4,5) 是路径中的最大值。
# 节点 3 -> (3,1,3) 是路径中的最大值。
# 
# 示例 2：
# 
# 
# 
# 输入：root = [3,3,null,4,2]
# 输出：3
# 解释：节点 2 -> (3, 3, 2) 不是好节点，因为 "3" 比它大。
# 
# 示例 3：
# 
# 输入：root = [1]
# 输出：1
# 解释：根节点是好节点。
# 
# 
# 
# 提示：
# 
# 
# 二叉树中节点数目范围是 [1, 10^5] 。
# 每个节点权值的范围是 [-10^4, 10^4] 。
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

# DFS
# T:O(N) S:O(N)
class Solution:
    def __init__(self):
        self.counter = 0

    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node:TreeNode, max_value:int) -> int:
            if not node: return
            else:
                # 如果存在比当前值大的计数器+1
                if node.val>=max_value:
                    self.counter += 1
                    max_value=node.val
                # 递归到叶子为止
                dfs(node.left, max_value)
                dfs(node.right, max_value)
        # 最小值切入
        dfs(root, float('-inf'))
        return self.counter
# @lc code=end

