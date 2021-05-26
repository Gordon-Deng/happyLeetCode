#
# @lc app=leetcode.cn id=1190 lang=python3
#
# [1190] 反转每对括号间的子串
#
# https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/
#
# algorithms
# Medium (59.41%)
# Likes:    163
# Dislikes: 0
# Total Accepted:    33.6K
# Total Submissions: 51.9K
# Testcase Example:  '"(abcd)"'
#
# 给出一个字符串 s（仅含有小写英文字母和括号）。
# 
# 请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
# 
# 注意，您的结果中 不应 包含任何括号。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "(abcd)"
# 输出："dcba"
# 
# 
# 示例 2：
# 
# 输入：s = "(u(love)i)"
# 输出："iloveu"
# 
# 
# 示例 3：
# 
# 输入：s = "(ed(et(oc))el)"
# 输出："leetcode"
# 
# 
# 示例 4：
# 
# 输入：s = "a(bcdefghijkl(mno)p)q"
# 输出："apmnolkjihgfedcbq"
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= s.length <= 2000
# s 中只有小写英文字母和括号
# 我们确保所有括号都是成对出现的
# 
# 
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        n = len(s)
        pair = [0] * n

        # 预先存储左右括号的映射关系
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            if s[i] == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i 
        
        index = 0
        # step = 1 表示向右走, step = -1 表示向左走
        step = 1
        result = []
        while index < n:
            if s[index] == '(' or s[index] == ')':
                index = pair[index]
                # 走的方向反转
                step = -step
            else:
                result.append(s[index])
            index += step
        return "".join(result)
# @lc code=end

