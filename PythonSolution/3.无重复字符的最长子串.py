#
# @lc app=leetcode.cn id=3 lang=python3
#
[3] 无重复字符的最长子串

https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/

algorithms
Medium (32.44%)
Likes:    2984
Dislikes: 0
Total Accepted:    316.5K
Total Submissions: 975.2K
Testcase Example:  '"abcabcbb"'

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        cur_len = 0
        max_len = 0
        left = 0
        n = len(s)
        flag = set()

        for i in range(n):
            cur_len += 1
            while s[i] in flag:
                flag.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:  max_len = cur_len
            flag.add(s[i])
        return max_len
# @lc code=end

