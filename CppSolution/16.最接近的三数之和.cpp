/*
 * @lc app=leetcode.cn id=16 lang=cpp
 *
 * [16] 最接近的三数之和
 *
 * https://leetcode-cn.com/problems/3sum-closest/description/
 *
 * algorithms
 * Medium (42.47%)
 * Likes:    358
 * Dislikes: 0
 * Total Accepted:    72.7K
 * Total Submissions: 169.5K
 * Testcase Example:  '[-1,2,1,-4]\n1'
 *
 * 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
 * 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
 * 
 * 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
 * 
 * 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
 * 
 * 
 */

// @lc code=start
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int len = nums.size();
        if(len < 3)
            return 0;
        sort(nums.begin(), nums.end());
        int i, low, high;
        int delta = 0x7fffffff, sum, ans;
        for(i = 0; i < len - 2; i++){
            low = i + 1;
            high = len - 1;
            while(low < high){
                sum = nums[i] + nums[low] + nums[high];
                if(sum == target){
                    return sum;
                }
                else if(sum < target){
                    if(target - sum < delta){
                        delta = target - sum;
                        ans = sum;
                    }
                    low++;
                }
                else{
                    if(sum - target < delta){
                        delta = sum - target;
                        ans = sum;
                    }
                    high--;
                }
            }
        }
        return ans;
    }
};
// @lc code=end

