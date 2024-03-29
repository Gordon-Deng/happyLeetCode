#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (38.08%)
# Likes:    288
# Dislikes: 0
# Total Accepted:    38.2K
# Total Submissions: 99.6K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
# 
# 示例 1:
# 
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 
# 
# 示例 2:
# 
# 输入:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or 0 == len(matrix):
            return list()
        r, l = len(matrix),  len(matrix[0])
        res = list()

        left, right, top, bottom = 0, l-1, 0, r-1

        while left <= right and top <= bottom:
            for colum in range(left, right+1):
                res.append(matrix[top][colum])
            for row in range(top+1, bottom + 1):
                res.append(matrix[row][right])
            if left < right and top < bottom:
                for colum_ in range(right-1, left, -1):
                    res.append(matrix[bottom][colum_])
                for row_ in range(bottom, top, -1):
                    res.append(matrix[row_][left])

            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return res
# @lc code=end

