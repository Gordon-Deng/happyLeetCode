#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (58.91%)
# Likes:    333
# Dislikes: 0
# Total Accepted:    39.3K
# Total Submissions: 66.5K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 
# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
# 
# 
# 
# 
# 
# 示例 1:
# 
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
# 
# 
# 示例 2:
# 
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
# 
# 
# 
# 
# 说明:
# 
# 
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。
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

#由于每个节点只有唯一一个父节点，我们可以使用到字典的value-key的形式（节点-父节点）
#字典中预置根节点的父节点为None。

#字典建立完成后，二叉树就可以看成一个所有节点都将最终指向根节点的链表了。

#于是在二叉树中寻找两个节点的最小公共节点就相当于，在一个链表中寻找他们相遇的节点

# 然后就是双链表的查交叉了
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic = {root:None}
        def dfs(node):
            if node:
                if node.left: 
                    dic[node.left] = node
                if node.right: 
                    dic[node.right] = node
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        l1, l2 = p, q
        while(l1!=l2):
            l1 = dic.get(l1, q)
            l2 = dic.get(l2, p)
        return l1 
# @lc code=end

