#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (50.77%)
# Likes:    1774
# Dislikes: 0
# Total Accepted:    318.2K
# Total Submissions: 626.5K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7]
# 的子序列。
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10^4 
# 
# 
# 
# 
# 进阶：
# 
# 
# 你可以设计时间复杂度为 O(n^2) 的解决方案吗？
# 你能将算法的时间复杂度降低到 O(n log(n)) 吗?
# 
# 
#

# @lc code=start
#  动态规划表的表项含义不是“前n个数的最大上升子序长度”，而是“以nums[i]结尾的最大上升子序列长度”，强调你选的子序列一定是以i结尾的，而最终答案的最优子序列不一定是以nums最后一项结尾，所以要找dptable里的max
# 0 1 0 3 2 3
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]: # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
# @lc code=end

