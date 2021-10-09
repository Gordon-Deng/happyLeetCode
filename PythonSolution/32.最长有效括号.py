#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (35.09%)
# Likes:    1347
# Dislikes: 0
# Total Accepted:    159.5K
# Total Submissions: 454.1K
# Testcase Example:  '"(()"'
#
# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
# 
# 
# 示例 2：
# 
# 
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
# 
# 
# 示例 3：
# 
# 
# 输入：s = ""
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# s[i] 为 '(' 或 ')'
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        res = 0
        for i in range(n):
            if i>0 and s[i] == ")":
                if  s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        return res  
# @lc code=end

