/*
 * @lc app=leetcode.cn id=59 lang=cpp
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
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        // 创建二维矩阵
        // vector<vector<int>> matrix(n);
        // for (int i = 0; i < matrix.size(); i++)
        //     matrix[i].resize(n);

        vector<vector<int>> matrix(n,vector<int>(n));
        // 上下左右
        int u = 0;
        int d = n-1;
        int l = 0;
        int r = n-1;
        int num = 1;

        while(num <= n*n){
            // 上
            for(int i=l; i <= r; i++) matrix[u][i] = num++;
            if (u++ >= d) break;
            // 右
            for(int i=u; i <= d; i++) matrix[i][r] = num++;
            if (r-- <= l) break;
            // 下
            for(int i=r; i >= l; i--) matrix[d][i] = num++;
            if (d-- <= u) break;
            // 左
            for(int i=d; i >= u; i--) matrix[i][l] = num++;
            if (l++ >= r) break;
        }
        return matrix;
    }
};
// @lc code=end

