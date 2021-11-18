#
# @lc app=leetcode.cn id=5 lang=python3
#
[5] 最长回文子串

https://leetcode-cn.com/problems/longest-palindromic-substring/description/

algorithms
Medium (28.04%)
Likes:    1622
Dislikes: 0
Total Accepted:    165.2K
Total Submissions: 588K
Testcase Example:  '"babad"'

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。


示例 2：

输入: "cbbd"
输出: "bb"




# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len, begin_index = 1, 0
        dp = [[False] * n for _ in range(n)]
        # if s[0] == s[1]:
        #     dp[0][1] = True

        for i in range(n):
            dp[i][i] = True
        for L in range(2, n+1):
            for i in range(n):
                j = L + i - 1
                if j >= n:
                    break
                if s[i] == s[j] and (j - i < 3):
                    dp[i][j] = True
                elif s[i] == s[j] and (j - i >= 3):
                    dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin_index = i
        return s[begin_index:begin_index + max_len]
# @lc code=end

