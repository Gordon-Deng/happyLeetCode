#
# @lc app=leetcode.cn id=407 lang=python3
#
# [407] 接雨水 II
#
# https://leetcode-cn.com/problems/trapping-rain-water-ii/description/
#
# algorithms
# Hard (47.75%)
# Likes:    356
# Dislikes: 0
# Total Accepted:    9.1K
# Total Submissions: 18.9K
# Testcase Example:  '[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]'
#
# 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。
# 
# 
# 
# 示例：
# 
# 给出如下 3x6 的高度图:
# [
# ⁠ [1,4,3,1,3,2],
# ⁠ [3,2,1,3,2,4],
# ⁠ [2,3,3,2,3,1]
# ]
# 
# 返回 4 。
# 
# 
# 
# 
# 如上图所示，这是下雨前的高度图[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] 的状态。
# 
# 
# 
# 
# 
# 下雨后，雨水将会被存储在这些方块中。总的接雨水量是4。
# 
# 
# 
# 提示：
# 
# 
# 1 <= m, n <= 110
# 0 <= heightMap[i][j] <= 20000
# 
# 
#

# @lc code=start
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
# @lc code=end

