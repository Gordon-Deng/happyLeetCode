/*
 * @lc app=leetcode.cn id=169 lang=cpp
 *
 * [169] 多数元素
 *
 * https://leetcode-cn.com/problems/majority-element/description/
 *
 * algorithms
 * Easy (61.05%)
 * Likes:    445
 * Dislikes: 0
 * Total Accepted:    110K
 * Total Submissions: 178.5K
 * Testcase Example:  '[3,2,3]'
 *
 * 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
 * 
 * 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
 * 
 * 示例 1:
 * 
 * 输入: [3,2,3]
 * 输出: 3
 * 
 * 示例 2:
 * 
 * 输入: [2,2,1,1,1,2,2]
 * 输出: 2
 * 
 * 
 */

// @lc code=start
class Solution
{
public:
    int majorityElement(vector<int> &nums)
    {
        int candidate = nums.at(0);
        int count = 1;
        for (int i = 1; i < nums.size(); ++i)
        {
            if (count == 0)
            {
                candidate = nums.at(i);
                count = 1;
            }

            else if (nums.at(i) == candidate) //注意：不能写成if 避免count==0后又进入此分支，使count变为2
                ++count;

            else
                --count;
        }
        return candidate;
    }
};
// @lc code=end
