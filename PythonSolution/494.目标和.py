#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#
# https://leetcode-cn.com/problems/target-sum/description/
#
# algorithms
# Medium (46.13%)
# Likes:    792
# Dislikes: 0
# Total Accepted:    114.4K
# Total Submissions: 232.4K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 给你一个整数数组 nums 和一个整数 target 。
# 
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
# 
# 
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 
# 
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1], target = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 0 
# -1000 
# 
# 
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #正数和为x，负数和绝对值为y   x + y = sum(nums)  x - y = target   x = (sum+target)/2
        tot_sum = sum(nums)
        if tot_sum < target :
            return 0
        positive_sum = (tot_sum + target) // 2
        if (tot_sum + target) % 2 == 1:
            return 0
        
        dp = [0 for _ in range(positive_sum + 1)]
        dp[0] = 1 
        for num in nums:
            for x in range(positive_sum, num - 1, -1):
                dp[x] += dp[x-num]
        return dp[positive_sum]

# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         s = sum(nums)
#         dp = [collections.defaultdict(int) for i in range(len(nums))]

#         dp[0][nums[0]] = 1
#         dp[0][-nums[0]] +=1

#         for i in range(1, len(nums)):
#             for key in dp[i - 1]:
#                 dp[i][key + nums[i]] += dp[i - 1][key]
#                 dp[i][key - nums[i]] += dp[i - 1][key]

#         return dp[-1][target]
# @lc code=end

