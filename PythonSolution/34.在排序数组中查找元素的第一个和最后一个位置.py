#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (42.52%)
# Likes:    1174
# Dislikes: 0
# Total Accepted:    320.1K
# Total Submissions: 753.9K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 
# 进阶：
# 
# 
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 
# 示例 2：
# 
# 
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 
# 示例 3：
# 
# 
# 输入：nums = [], target = 0
# 输出：[-1,-1]
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^9 
# nums 是一个非递减数组
# -10^9 
# 
# 
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or nums[0] > target or nums[-1] < target:
            return [-1,-1]
        # 找第一个/最后一个元素位置 二分法 老套路
        def findEdge(l,r,left):
            while l < r:
                mid = (l+r)//2 if left else (l+r+1)//2   # 防止一直在同一个位置循环
                if nums[mid] == target:
                    if left:
                        r = mid   # 第一个元素位置 <= mid
                    else:
                        l = mid   # 最后一个元素位置 >= mid
                elif nums[mid] > target:
                    r = mid -1
                else:
                    l = mid + 1
            return l if nums[l] == target else -1

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:   # 转用方法二
                first = findEdge(l, r,True)
                last = findEdge(l, r,False)
                return [first,last]
            elif nums[mid] < target:                # l,r 都在mid右边
                l = mid + 1
            else:                                   # l,r 都在mid左边
                r = mid - 1
        return [-1,-1]
# @lc code=end

