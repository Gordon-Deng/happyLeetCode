#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#
# https://leetcode-cn.com/problems/ones-and-zeroes/description/
#
# algorithms
# Medium (56.85%)
# Likes:    487
# Dislikes: 0
# Total Accepted:    58K
# Total Submissions: 97.7K
# Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
#
# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
# 
# 
# 请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。
# 
# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
# 输出：4
# 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
# 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于
# n 的值 3 。
# 
# 
# 示例 2：
# 
# 
# 输入：strs = ["10", "0", "1"], m = 1, n = 1
# 输出：2
# 解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# strs[i] 仅由 '0' 和 '1' 组成
# 1 
# 
# 
#

# @lc code=start

# 传统做法
# python的入门坑。 dp = [[]]*3表示开辟三份地址，且地址相同。所以你改动一个，就全改。最内层可以用 [ ] *，最外层必须用 for _ in range()
# T:O(lmn+L) S:O(mn)
# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
#         for s in strs:
#             cnt0 = s.count('0')
#             cnt1 = s.count('1')
#             for i in range(m, cnt0 - 1, -1):    #0-1背包问题，内循环逆序
#                 for j in range(n, cnt1 - 1, -1):
#                     dp[i][j] = max(dp[i][j], dp[i-cnt0][j-cnt1] + 1)
#         return dp[m][n]

# 让面试官一亮的做法
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count = [Counter(s) for s in strs]
        @cache
        def dpCache(m, n, i):
            if i < 0 or (not m and not n):
                return 0
            elif m < (M := count[i]['0']) or n < (N := count[i]['1']):
                return dpCache(m, n, i - 1)
            else:
                return max(dpCache(m, n, i - 1), 1 + dpCache(m - M, n - N, i - 1))
        return dpCache(m, n, len(strs) - 1)
# @lc code=end

