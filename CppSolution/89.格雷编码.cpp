/*
 * @lc app=leetcode.cn id=89 lang=cpp
 *
 * [89] 格雷编码
 *
 * https://leetcode-cn.com/problems/gray-code/description/
 *
 * algorithms
 * Medium (67.23%)
 * Likes:    128
 * Dislikes: 0
 * Total Accepted:    18.5K
 * Total Submissions: 27.3K
 * Testcase Example:  '2'
 *
 * 格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
 * 
 * 给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。
 * 
 * 示例 1:
 * 
 * 输入: 2
 * 输出: [0,1,3,2]
 * 解释:
 * 00 - 0
 * 01 - 1
 * 11 - 3
 * 10 - 2
 * 
 * 对于给定的 n，其格雷编码序列并不唯一。
 * 例如，[0,2,3,1] 也是一个有效的格雷编码序列。
 * 
 * 00 - 0
 * 10 - 2
 * 11 - 3
 * 01 - 1
 * 
 * 示例 2:
 * 
 * 输入: 0
 * 输出: [0]
 * 解释: 我们定义格雷编码序列必须以 0 开头。
 * 给定编码总位数为 n 的格雷编码序列，其长度为 2^n。当 n = 0 时，长度为 2^0 = 1。
 * 因此，当 n = 0 时，其格雷编码序列为 [0]。
 * 
 * 
 */

// @lc code=start
class Solution
{
public:
    vector<int> grayCode(int n)
    {
        int total = 1;
        for (int i = 0; i < n; i++)
            total *= 2;
        vector<int> ans(total, 0);
        trackback(ans, n - 1, 0, total - 1);
        return ans;
    }
    void trackback(vector<int> &ans, int n, int left, int right)
    {
        if (n < 0)
            return;
        int m1 = (1 << n);
        int mid = (left + right) / 2;
        for (int i = mid + 1; i <= right; i++)
            ans[i] = (ans[i] | m1);
        trackback(ans, n - 1, left, mid);              //对前一半进行迭代，因为前一半的第n-1位应该是先0后1;
        trackback_reverse(ans, n - 1, mid + 1, right); //对后一半进行迭代，第n-1位是先1后0；
    }
    void trackback_reverse(vector<int> &ans, int n, int left, int right)
    {
        if (n < 0)
            return;
        int m1 = (1 << n);
        int mid = (left + right) / 2;
        for (int i = left; i <= mid; i++)
            ans[i] = (ans[i] | m1);
        trackback(ans, n - 1, left, mid);              //对前一半进行迭代，因为前一半的第n-1位应该是先0后1;
        trackback_reverse(ans, n - 1, mid + 1, right); //对后一半进行迭代，第n-1位是先1后0；
    }
};
// @lc code=end