#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#
# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (56.35%)
# Likes:    505
# Dislikes: 0
# Total Accepted:    74.2K
# Total Submissions: 131.6K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
# 
# 
# 
# 示例：
# 
# 输入：
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出：3
# 解释：
# 长度最长的公共子数组是 [3, 2, 1] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
# 
# 
#

# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i+1][j+1] + 1  if nums2[i] == nums1[j] else 0
                ans = max(dp[i][j], ans)
        return ans
# @lc code=end

