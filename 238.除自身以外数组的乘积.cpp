/*
 * @lc app=leetcode.cn id=238 lang=cpp
 *
 * [238] 除自身以外数组的乘积
 *
 * https://leetcode-cn.com/problems/product-of-array-except-self/description/
 *
 * algorithms
 * Medium (65.23%)
 * Likes:    298
 * Dislikes: 0
 * Total Accepted:    26.4K
 * Total Submissions: 40.1K
 * Testcase Example:  '[1,2,3,4]'
 *
 * 给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i]
 * 之外其余各元素的乘积。
 * 
 * 示例:
 * 
 * 输入: [1,2,3,4]
 * 输出: [24,12,8,6]
 * 
 * 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
 * 
 * 进阶：
 * 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
 * 
 */

// @lc code=start
// O(n) O(n)
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        int n=nums.size();
        int left=1,right=1;     //left：从左边累乘，right：从右边累乘
        vector<int> res(n,1);
        
        for(int i=0;i<n;++i)    //最终每个元素其左右乘积进行相乘得出结果
        {
            res[i]*=left;       //乘以其左边的乘积
            left*=nums[i];
            
            res[n-1-i]*=right;  //乘以其右边的乘积
            right*=nums[n-1-i];
        }
        
        return res;
        
    }
};
// @lc code=end

