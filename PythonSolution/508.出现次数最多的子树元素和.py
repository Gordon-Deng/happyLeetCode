#
# @lc app=leetcode.cn id=508 lang=python3
#
# [508] 出现次数最多的子树元素和
#
# https://leetcode-cn.com/problems/most-frequent-subtree-sum/description/
#
# algorithms
# Medium (66.65%)
# Likes:    109
# Dislikes: 0
# Total Accepted:    12.4K
# Total Submissions: 18.6K
# Testcase Example:  '[5,2,-3]'
#
# 给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。
# 
# 你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。
# 
# 
# 
# 示例 1：
# 输入:
# 
# ⁠ 5
# ⁠/  \
# 2   -3
# 
# 
# 返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。
# 
# 示例 2：
# 输入：
# 
# ⁠ 5
# ⁠/  \
# 2   -5
# 
# 
# 返回 [2]，只有 2 出现两次，-5 只出现 1 次。
# 
# 
# 
# 提示： 假设任意子树元素和均可以用 32 位有符号整数表示。
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
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        
        # 生成默认的字典 相当于 java中的 Map.getOrDefault(key,0)
        tree_dict = collections.defaultdict(int)
        
        # 递归 遍历出所有 子的元素和 并用 字典记录
        def helper(root):
            if not root:return 0
            left = helper(root.left)
            right = helper(root.right)
            temp = left + right + root.val
            tree_dict[temp] += 1
            return temp
        if not root:return []
        helper(root)
        
        # 记录出现最多次的 子树的元素和
        tree_max = 0
        # python 通过 dict.values() 遍历出字典中的 value 
        # 类似于 java中的 for(Map.Entry<String, String> entry : map.entrySet())
        for cnt in tree_dict.values():
            tree_max = max(cnt,tree_max)
        res_list = []
        
        # python 通过 dict.items() 遍历出字典中的key 和 value
        for key, val in tree_dict.items():
            if val == tree_max:
                res_list.append(key)
        return res_list
# @lc code=end

