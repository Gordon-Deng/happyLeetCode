#
# @lc app=leetcode.cn id=1104 lang=python3
#
# [1104] 二叉树寻路
#
# https://leetcode-cn.com/problems/path-in-zigzag-labelled-binary-tree/description/
#
# algorithms
# Medium (71.24%)
# Likes:    68
# Dislikes: 0
# Total Accepted:    7.7K
# Total Submissions: 10.7K
# Testcase Example:  '14'
#
# 在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。
# 
# 如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；
# 
# 而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。
# 
# 
# 
# 给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。
# 
# 
# 
# 示例 1：
# 
# 输入：label = 14
# 输出：[1,3,4,14]
# 
# 
# 示例 2：
# 
# 输入：label = 26
# 输出：[1,2,6,10,26]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= label <= 10^6
# 
# 
#

# @lc code=start

# res[::-1]倒序 math.log2()求底数  // 2整除

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:    
        if label == 0: return []
        if label == 1: return [1]
        
        res = [label]
        while label > 1:
            # label所属level
            level = int(math.log2(label))
            # label行最小值
            level_start = 2 ** level
            # label与该行最小值的差值整除2， 用于得到上一行连接label的数字
            remain = (label - level_start) // 2
            
            # 迭代label
            label = level_start - 1 - remain
            res.append(label)
        
        return res[::-1]
# @lc code=end

