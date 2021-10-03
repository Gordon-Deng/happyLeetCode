#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#
# https://leetcode-cn.com/problems/max-consecutive-ones-iii/description/
#
# algorithms
# Medium (59.87%)
# Likes:    324
# Dislikes: 0
# Total Accepted:    67.1K
# Total Submissions: 112.5K
# Testcase Example:  '[1,1,1,0,0,0,1,1,1,1,0]\n2'
#
# 给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
# 
# 返回仅包含 1 的最长（连续）子数组的长度。
# 
# 
# 
# 示例 1：
# 
# 输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释： 
# [1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。
# 
# 示例 2：
# 
# 输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# 输出：10
# 解释：
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 10。
# 
# 
# 
# 提示：
# 
# 
# 
# 1 <= A.length <= 20000
# 0 <= K <= A.length
# A[i] 为 0 或 1 
# 
# 
#

# @lc code=start

# https://leetcode-cn.com/problems/max-consecutive-ones-iii/solution/fen-xiang-hua-dong-chuang-kou-mo-ban-mia-f76z/
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if not nums or n == 0:
            return 0
        left, right = 0, 0
        sum = 0
        zero_count = 0

        while left <= right and right < n:
            if nums[right] == 0 and zero_count < k:
                right += 1
                zero_count += 1
            elif nums[right] == 0 and zero_count == k and nums[left] == 0:
                left += 1
                zero_count -= 1
            elif nums[right] == 0 and zero_count == k and nums[left] == 0:
                left += 1       
                zero_count += 1
            else : 
                right += 1
                sum = max(sum, right-left+1)

        return sum
# @lc code=end

