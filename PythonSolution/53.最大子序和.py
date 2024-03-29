#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (48.60%)
# Likes:    1630
# Dislikes: 0
# Total Accepted:    161.2K
# Total Submissions: 327.5K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
#

# @lc code=start
from typing import List

# 不好
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         size = len(nums)
#         dp = [0] * len(nums)
#         for i in range(size):
#             # 这里不用PRE的话，会出现o(n)的时间复杂度
#             dp[i] = max(nums[i], dp[i-1] + nums[i])
#         return max(dp)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        pre = 0
        res = nums[0]
        for i in range(size):
            # 这里不用PRE的话，会出现o(n)的时间复杂度
            pre = max(nums[i], pre + nums[i])
            res = max(res, pre)
        return res
# @lc code=end

