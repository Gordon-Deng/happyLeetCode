/*
 * @lc app=leetcode.cn id=46 lang=java
 *
 * [46] 全排列
 *
 * https://leetcode-cn.com/problems/permutations/description/
 *
 * algorithms
 * Medium (73.45%)
 * Likes:    530
 * Dislikes: 0
 * Total Accepted:    77.2K
 * Total Submissions: 104.3K
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一个没有重复数字的序列，返回其所有可能的全排列。
 * 
 * 示例:
 * 
 * 输入: [1,2,3]
 * 输出:
 * [
 * ⁠ [1,2,3],
 * ⁠ [1,3,2],
 * ⁠ [2,1,3],
 * ⁠ [2,3,1],
 * ⁠ [3,1,2],
 * ⁠ [3,2,1]
 * ]
 * 
 */

// @lc code=start

// 位运算真牛逼
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        int len = nums.length;
        if (len == 0)
            return Collections.emptyList();

        List<List<Integer>> res = new LinkedList<>();
        bt(nums, new Integer[len], 0, 0b0, res);
        return res;
    }

    private void bt(int[] nums, Integer[] curr, int ci, int occupy, List<List<Integer>> res) {
        if (occupy == (1 << nums.length) - 1) { // 每个数都选了
            res.add(new ArrayList<>(Arrays.asList(curr)));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (((occupy >> i) & 1) == 1)
                continue; // 已选中
            occupy |= 1 << i; // 勾选
            curr[ci] = nums[i];
            bt(nums, curr, ci + 1, occupy, res);
            occupy &= (~(1 << i)); // 去选
        }
    }
}
// @lc code=end

