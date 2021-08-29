#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (47.10%)
# Likes:    704
# Dislikes: 0
# Total Accepted:    159.2K
# Total Submissions: 335.8K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n' +
  '5'
#
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
# 
# 
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 5
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 20
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# -10^9 
# 每行的所有元素从左到右升序排列
# 每列的所有元素从上到下升序排列
# -10^9 
# 
# 
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height-1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else: # found it
                return True
        
        return False
# @lc code=end

