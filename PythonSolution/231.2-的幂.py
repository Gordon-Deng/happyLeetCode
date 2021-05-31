#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (47.28%)
# Likes:    162
# Dislikes: 0
# Total Accepted:    45.8K
# Total Submissions: 96.2K
# Testcase Example:  '1'
#
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
# 
# 示例 1:
# 
# 输入: 1
# 输出: true
# 解释: 2^0 = 1
# 
# 示例 2:
# 
# 输入: 16
# 输出: true
# 解释: 2^4 = 16
# 
# 示例 3:
# 
# 输入: 218
# 输出: false
# 
#

# @lc code=start

# n & (n - 1) 将n 二进制表示的最低位 11 移除
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

# n & (-n) 获取 n 二进制表示的最低位的 11
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return n > 0 and (n & -n) == n
# @lc code=end

