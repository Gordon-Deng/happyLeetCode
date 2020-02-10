/*
 * @lc app=leetcode.cn id=78 lang=cpp
 *
 * [78] 子集
 *
 * https://leetcode-cn.com/problems/subsets/description/
 *
 * algorithms
 * Medium (75.86%)
 * Likes:    463
 * Dislikes: 0
 * Total Accepted:    58.9K
 * Total Submissions: 77.2K
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
 * 
 * 说明：解集不能包含重复的子集。
 * 
 * 示例:
 * 
 * 输入: nums = [1,2,3]
 * 输出:
 * [
 * ⁠ [3],
 * [1],
 * [2],
 * [1,2,3],
 * [1,3],
 * [2,3],
 * [1,2],
 * []
 * ]
 * 
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> ans;
    vector<int> tmp;
    void find(int dep, vector<int>& nums)
    {
        // 已经处理完最后一位，将目前存储的集合存入 ans ，并回溯
        if(dep <= 0)
        {
            ans.push_back(tmp);
            return;
        }
        // 情况一：集合中有该元素
        tmp.push_back(nums[dep - 1]);
        find(dep - 1, nums);
        tmp.pop_back();
        // 情况二：集合中无该元素
        find(dep - 1, nums);
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        find(nums.size(), nums);
        return ans;
    }
};
// @lc code=end

