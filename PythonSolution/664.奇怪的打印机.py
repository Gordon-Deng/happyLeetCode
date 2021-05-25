#
# @lc app=leetcode.cn id=664 lang=python3
#
# [664] 奇怪的打印机
#
# https://leetcode-cn.com/problems/strange-printer/description/
#
# algorithms
# Hard (49.12%)
# Likes:    199
# Dislikes: 0
# Total Accepted:    18.9K
# Total Submissions: 29K
# Testcase Example:  '"aaabbb"'
#
# 有台奇怪的打印机有以下两个特殊要求：
# 
# 
# 打印机每次只能打印由 同一个字符 组成的序列。
# 每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。
# 
# 
# 给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。
# 
# 
# 示例 1：
# 
# 
# 输入：s = "aaabbb"
# 输出：2
# 解释：首先打印 "aaa" 然后打印 "bbb"。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "aba"
# 输出：2
# 解释：首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 由小写英文字母组成
# 
# 
#

# @lc code=start

# def helper(self, ns: List[int]) :
#     N = len(ns)
#     dp = [[0] * N for _ in range(N+1)]
#     for l in range(N): # 长度从小到大
#         for i in range(N-l): # 以 i 为 开头
#             j = i + l           # 以 j 为 终点
#             for k in range(i,j): # 以 k 为分割点，进行分治         
#                 // Todo 业务逻辑

class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s: return 0
        N = len(s)
        dp = [[0]*(N) for i in range(N+1)]
        for l in range(N):     # 区间长度
            for i in range(N-l):  # 区间起点
                j = i + l            # 区间终点
                dp[i][j] = dp[i+1][j] + 1 # 初始化
                for k in range(i+1, j+1):   # 枚举分割点
                    if s[k] == s[i]:    # 首位一样可减少一次
                        dp[i][j] = min(dp[i][j], dp[i][k-1]+dp[k+1][j])
        return dp[0][-1]
# @lc code=end

