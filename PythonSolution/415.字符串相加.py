#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (53.36%)
# Likes:    423
# Dislikes: 0
# Total Accepted:    136.6K
# Total Submissions: 255.6K
# Testcase Example:  '"11"\n"123"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
# 
# 
# 
# 提示：
# 
# 
# num1 和num2 的长度都小于 5100
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式
# 
# 
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j = len(num1)-1, len(num2)-1
        carry = 0
        while i>=0 or j>=0 or carry !=0:
            sub_add_num1 = int(num1[i]) if i>=0 else 0
            sub_add_num2 = int(num2[j]) if j>=0 else 0
            temp = sub_add_num1+sub_add_num2+carry
            carry = temp // 10
            res = str(temp%10) + res
            i, j = i-1, j-1
        return res
# @lc code=end

