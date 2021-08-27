#
# @lc app=leetcode.cn id=470 lang=python3
#
# [470] 用 Rand7() 实现 Rand10()
#
# https://leetcode-cn.com/problems/implement-rand10-using-rand7/description/
#
# algorithms
# Medium (55.31%)
# Likes:    225
# Dislikes: 0
# Total Accepted:    33.1K
# Total Submissions: 59.5K
# Testcase Example:  '1'
#
# 已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。
# 
# 不要使用系统的 Math.random() 方法。
# 
# 
# 
# 
# 
# 
# 示例 1:
# 
# 
# 输入: 1
# 输出: [7]
# 
# 
# 示例 2:
# 
# 
# 输入: 2
# 输出: [8,4]
# 
# 
# 示例 3:
# 
# 
# 输入: 3
# 输出: [8,1,10]
# 
# 
# 
# 
# 提示:
# 
# 
# rand7 已定义。
# 传入参数: n 表示 rand10 的调用次数。
# 
# 
# 
# 
# 进阶:
# 
# 
# rand7()调用次数的 期望值 是多少 ?
# 你能否尽量少调用 rand7() ?
# 
# 
#

# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        num = (rand7() - 1) * 49 +(rand7() - 1) * 7 + rand7() - 1 # 取得0-342之间的数字
        while num > 339: # 如数字>339 （340-342），舍弃，重新选取
            num =  (rand7() - 1) * 49 +(rand7() - 1) * 7 + rand7() - 1     
        # 如数字在0-339之间，模10加一，恰好可以等概率取得1-10之间的十个数字
        return num % 10 + 1  
# @lc code=end

