#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
# https://leetcode-cn.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (25.73%)
# Likes:    321
# Dislikes: 0
# Total Accepted:    39.2K
# Total Submissions: 122.1K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：3
# 
# 
# 示例 2：
# 
# 
# 输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出：4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# points[i].length == 2
# -10^4 i, yi 
# points 中的所有点 互不相同
# 
# 
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 1
        for i in range(len(points) - 1):
            curr = Counter()
            for j in range(i+1, len(points)):
                dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
                curr[dy / dx if dx else inf] += 1
            ans = max(ans, max(curr.values()) + 1)
        return ans
# @lc code=end

