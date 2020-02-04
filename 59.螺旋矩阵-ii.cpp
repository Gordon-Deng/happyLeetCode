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
        vector<vector<int>> ans;
        vector<int> tmp;
        int x, y, dir;
        int dx[4] = {0, 1, 0, -1};
        int dy[4] = {1, 0, -1, 0};
        for(x = 0; x < n; x ++)
            tmp.push_back(0);
        for(x = 0; x < n; x ++)
            ans.push_back(tmp);
        x = 0, y = 0, dir = 0;
        ans[0][0] = 1;
        for(int i = 2; i <= n * n; i ++)
        {
            if(x + dx[dir] < 0 || x + dx[dir] >= n || y + dy[dir] < 0 || y + dy[dir] >= n )
                dir = (dir + 1) % 4;
            else if(ans[x + dx[dir]][y + dy[dir]] > 0)
                dir = (dir + 1) % 4;
            x += dx[dir], y += dy[dir];
            ans[x][y] = i;
        }
        return ans;
    }
};
// @lc code=end

