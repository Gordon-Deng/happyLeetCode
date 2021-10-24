/*
 * @lc app=leetcode.cn id=46 lang=cpp
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

// T:O() S:O()
class Solution {
public:

    // 这个用STL做的，不太推荐
    // vector<vector<int>> permute(vector<int>& nums) {
    //     vector<vector<int>>ret;
    //     sort(nums.begin(),nums.end());
    //     do{
    //         ret.push_back(nums);
    //     }while(next_permutation(nums.begin(),nums.end()));
    //     return ret;
    // }
    using vec_iter = vector<vector<int>>::iterator;

    int get_factorial(int num)
    {
        int fac = 1;
        for (int i = 1; i <= num; ++i)
        {
            fac *= i;
        }

        return fac;
    }

    void _fill_leader_recursively(vec_iter group_iter, size_t group_size,
                                  list<int> &candidates, int leader = -1, bool entry = true)
    {
        // fill leader
        if (!entry)
        {
            for (int i = 0; i < group_size; ++i)
            {
                *((*(group_iter + i)).rbegin() + candidates.size()) = leader;
            }
        }

        // divide into groups
        if (!candidates.empty())
        {
            int sub_group_size = group_size / candidates.size();
            for (int i = 0; i < group_size; i += sub_group_size)
            {
                int sub_leader = *candidates.begin();
                candidates.pop_front();
                _fill_leader_recursively(group_iter + i, sub_group_size, candidates, sub_leader, false);
                candidates.push_back(sub_leader);
            }
        }
    }

    vector<vector<int>> permute(vector<int> &nums)
    {
        int res_size = get_factorial(nums.size());
        vector<vector<int>> results(res_size, vector<int>(nums.size(), 0));
        list<int> nums_list(nums.begin(), nums.end());
        _fill_leader_recursively(results.begin(), results.size(), nums_list);

        return results;
    }

};
// @lc code=end

