#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (47.85%)
# Likes:    858
# Dislikes: 0
# Total Accepted:    53.4K
# Total Submissions: 110K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
# 
# 示例:
# 
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# 
#

# @lc code=start
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         ans = 0
#         left, right = 0, len(height) - 1
#         leftMax = rightMax = 0

#         while left < right:
#             leftMax = max(leftMax, height[left])
#             rightMax = max(rightMax, height[right])
#             if height[left] < height[right]:
#                 ans += leftMax - height[left]
#                 left += 1
#             else:
#                 ans += rightMax - height[right]
#                 right -= 1
        
#         return ans 

# 超时大法。。。
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         ans = 0
#         for i in range(len(height)):
#             max_left, max_right = 0,0
#             # 寻找 max_left
#             for j in range(0,i):
#                 max_left = max(max_left,height[j])
#             # 寻找 max_right
#             for j in range(i,len(height)):
#                 max_right = max(max_right,height[j])
#             if min(max_left,max_right) > height[i]:
#                 ans += min(max_left,max_right) - height[i]
        
#         return ans    

# DP
# T:O(N) S:O(N)
class Solution:
    def trap(self, height: List[int]) -> int:
        # 边界条件
        if not height: return 0
        n = len(height)
        maxleft = [0] * n
        maxright = [0] * n
        ans = 0
        # 初始化
        maxleft[0] = height[0]
        maxright[n-1] = height[n-1]
        # 设置备忘录，分别存储左边和右边最高的柱子高度
        for i in range(1,n):
            maxleft[i] = max(height[i],maxleft[i-1])
        for j in range(n-2,-1,-1):
            maxright[j] = max(height[j],maxright[j+1])
        # 一趟遍历，比较每个位置可以存储多少水
        for i in range(n):
            if min(maxleft[i],maxright[i]) > height[i]:
                ans += min(maxleft[i],maxright[i]) - height[i]
        return ans
# @lc code=end

