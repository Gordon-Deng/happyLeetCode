#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (72.75%)
# Likes:    758
# Dislikes: 0
# Total Accepted:    75.3K
# Total Submissions: 102.7K
# Testcase Example:  '3'
#
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
# 
# 例如，给出 n = 3，生成结果为：
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(temp, left_bracket, right_bracket):
            if len(temp) == 2*n:
                ans.append("".join(temp))
                return
            if left_bracket < n:
                temp.append("(")
                backtrack(temp, left_bracket+1, right_bracket)
                temp.pop()
            if right_bracket < left_bracket:
                temp.append(")")
                backtrack(temp, left_bracket, right_bracket+1)
                temp.pop()
        backtrack([], 0, 0)
        return ans
# @lc code=end

