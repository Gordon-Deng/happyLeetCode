/*
 * @lc app=leetcode.cn id=59 lang=java
 *
 * [59] 螺旋矩阵 II
 *
 * https://leetcode-cn.com/problems/spiral-matrix-ii/description/
 *
 * algorithms
 * Medium (75.99%)
 * Likes:    139
 * Dislikes: 0
 * Total Accepted:    24.2K
 * Total Submissions: 31.7K
 * Testcase Example:  '3'
 *
 * 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
 * 
 * 示例:
 * 
 * 输入: 3
 * 输出:
 * [
 * ⁠[ 1, 2, 3 ],
 * ⁠[ 8, 9, 4 ],
 * ⁠[ 7, 6, 5 ]
 * ]
 * 
 */

// @lc code=start

// T:O(N) S:O(N)
// 转圈圈
class Solution {
    public int[][] generateMatrix(int n) {
        int l = 0, r = n - 1, t = 0, b = n - 1;
        int[][] mat = new int[n][n];
        int num = 1, tar = n * n;
        while (num <= tar) {
            for (int i = l; i <= r; i++)
                mat[t][i] = num++; // left to right.
            t++;
            for (int i = t; i <= b; i++)
                mat[i][r] = num++; // top to bottom.
            r--;
            for (int i = r; i >= l; i--)
                mat[b][i] = num++; // right to left.
            b--;
            for (int i = b; i >= t; i--)
                mat[i][l] = num++; // bottom to top.
            l++;
        }
        return mat;
    }
}
// @lc code=end
