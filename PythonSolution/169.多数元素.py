#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素

# https://leetcode-cn.com/problems/majority-element/description/

# algorithms
# Easy (61.05%)
# Likes:    445
# Dislikes: 0
# Total Accepted:    110K
# Total Submissions: 178.5K
# Testcase Example:  '[3,2,3]'

# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

# 示例 1:

# 输入: [3,2,3]
# 输出: 3

# 示例 2:

# 输入: [2,2,1,1,1,2,2]
# 输出: 2
# 
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
# @lc code=end

