#
# @lc app=leetcode.cn id=41 lang=python3
#
# [5953] 子数组范围和
#
# https://leetcode-cn.com/problems/rings-and-rods/
#
# 给你一个整数数组 nums 。nums 中，子数组的 范围 是子数组中最大元素和最小元素的差值。
#
# 返回 nums 中 所有 子数组范围的 和 。
#
# 子数组是数组中一个连续 非空 的元素序列。
#  
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：4
# 解释：nums 的 6 个子数组如下所示：
# [1]，范围 = 最大 - 最小 = 1 - 1 = 0 
# [2]，范围 = 2 - 2 = 0
# [3]，范围 = 3 - 3 = 0
# [1,2]，范围 = 2 - 1 = 1
# [2,3]，范围 = 3 - 2 = 1
# [1,2,3]，范围 = 3 - 1 = 2
# 所有范围的和是 0 + 0 + 0 + 1 + 1 + 2 = 4
# 示例 2：

# 输入：nums = [1,3,3]
# 输出：4
# 解释：nums 的 6 个子数组如下所示：
# [1]，范围 = 最大 - 最小 = 1 - 1 = 0
# [3]，范围 = 3 - 3 = 0
# [3]，范围 = 3 - 3 = 0
# [1,3]，范围 = 3 - 1 = 2
# [3,3]，范围 = 3 - 3 = 0
# [1,3,3]，范围 = 3 - 1 = 2
# 所有范围的和是 0 + 0 + 0 + 2 + 0 + 2 = 4
# 示例 3：

# 输入：nums = [4,-2,-3,4,1]
# 输出：59
# 解释：nums 中所有子数组范围的和是 59

# 暴力
# 其实可以排一下序，但没必要了
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            min_ = nums[i]
            max_ = nums[i]
            for j in range(i + 1, n):
                min_ = min(min_, nums[j])
                max_ = max(max_, nums[j])
                res += (max_ - min_)
        return res

# 单调栈
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # 单调栈
        n = len(nums)
        #
        minleft, stack = [], []
        for i, num in enumerate(nums):
            while stack and num < nums[stack[-1]]:
                stack.pop()
            minleft.append(-1 if not stack else stack[-1])
            stack.append(i)
        minright, stack = [], []
        for i in range(n-1, -1, -1):
            num = nums[i]
            while stack and num <= nums[stack[-1]]:
                stack.pop()
            minright.append(n if not stack else stack[-1])
            stack.append(i)
        minright = minright[::-1]
        #
        maxleft, stack = [], []
        for i, num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                stack.pop()
            maxleft.append(-1 if not stack else stack[-1])
            stack.append(i)
        maxright, stack = [], []
        for i in range(n-1, -1, -1):
            num = nums[i]
            while stack and num >= nums[stack[-1]]:
                stack.pop()
            maxright.append(n if not stack else stack[-1])
            stack.append(i)
        maxright = maxright[::-1]
        #
        ans = 0
        for i in range(n):
            ans += nums[i] * ( (i-maxleft[i])*(maxright[i]-i) - (i-minleft[i])*(minright[i]-i) )
        return ans

# 滑动窗口
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            max_num, min_num = nums[i], nums[i]
            for j in range(i+1, n):
                max_num = max(max_num, nums[j])
                min_num = min(min_num, nums[j])
                result += (max_num-min_num)
        return result

# DP
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

