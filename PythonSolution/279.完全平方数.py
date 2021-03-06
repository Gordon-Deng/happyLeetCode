#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
# https://leetcode-cn.com/problems/perfect-squares/description/
#
# algorithms
# Medium (60.69%)
# Likes:    972
# Dislikes: 0
# Total Accepted:    164.2K
# Total Submissions: 264K
# Testcase Example:  '12'
#
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
# 
# 给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
# 
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11
# 不是。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 12
# 输出：3 
# 解释：12 = 4 + 4 + 4
# 
# 示例 2：
# 
# 
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start

# https://leetcode-cn.com/problems/perfect-squares/solution/gong-shui-san-xie-xiang-jie-wan-quan-bei-nqes/

# T:O(N*跟号N) S:O(N)
# 四平方和定理证明了任意一个正整数都可以被表示为至多四个正整数的平方和。这给出了本题的答案的上界。
class Solution:
    def numSquares(self, n: int) -> int:
        INF = 10 ** 9 + 7

        nums = []
        for x in range(1, int(n ** 0.5) + 1):
            nums.append(x ** 2)

        dp = [INF for _ in range(n + 1)]
        for x in nums:
            dp[x] = 1
            
        for i in range(1, n + 1):
            for j in nums:          #背包问题，可以顺序
                if i >= j:
                    dp[i] = min(dp[i], dp[i-j] + 1)
                else:
                    break
        return dp[n]
# @lc code=end

