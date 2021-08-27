#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (54.87%)
# Likes:    1296
# Dislikes: 0
# Total Accepted:    305.4K
# Total Submissions: 554.3K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 
# 此外，你可以假设该网格的四条边均被水包围。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 
# grid[i][j] 的值为 '0' 或 '1'
# 
# 
#

# @lc code=start
class Solution:
    def dfs(self, grid, r, c):
        row , column = len(grid), len(grid[0])
        grid[r][c] = 0
        for x, y in [(r -1, c), (r+1, c), (r, c - 1), (r, c+1)]:
            if 0<=x<row and 0<=y<column and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or 0 == len(grid[0]):
            return 0
        max_row, max_column = len(grid), len(grid[0])
        res = 0

        for i in range(max_row):
            for j in range(max_column):
                if grid[i][j] == "1":
                    res += 1
                    self.dfs(grid, i, j)
        return res
# @lc code=end

