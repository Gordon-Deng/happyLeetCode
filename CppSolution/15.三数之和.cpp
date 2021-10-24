/*
 * @lc app=leetcode.cn id=15 lang=cpp
 *
 * [15] 三数之和
 *
 * https://leetcode-cn.com/problems/3sum/description/
 *
 * algorithms
 * Medium (24.99%)
 * Likes:    1768
 * Dislikes: 0
 * Total Accepted:    152.6K
 * Total Submissions: 601.7K
 * Testcase Example:  '[-1,0,1,2,-1,-4]'
 *
 * 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
 * ？找出所有满足条件且不重复的三元组。
 * 
 * 注意：答案中不可以包含重复的三元组。
 * 
 * 
 * 
 * 示例：
 * 
 * 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
 * 
 * 满足要求的三元组集合为：
 * [
 * ⁠ [-1, 0, 1],
 * ⁠ [-1, -1, 2]
 * ]
 * 
 * 
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        if(nums.size() < 3) return res;
        sort(nums.begin(),nums.end());
        for(vector<int>::iterator it = nums.begin(); it != nums.end()-2;){
            int tmp = *it;
            if(tmp > 0) break;
            int target = 0 - tmp;
            vector<int>::iterator left = it+1;
            vector<int>::iterator right = nums.end()-1;
            while(left < right){
                if(*right < 0) break;//如果右边小于0，break
                if(*left + *right < target){
                    int v= *left;
                    while(left != right && *left == v) left++;//跳过相等的元素
                }else if(*left + *right > target){
                    int v= *right;
                    while(left != right && *right == v) right --;//跳过相等的元素
                }else{
                    vector<int> tmp_res{tmp,*left,*right};//保存结果
                    res.push_back(tmp_res);
                    int v= *left;
                    while(left != right &&  *left == v) left++;//跳过相等的元素
                    v= *right;
                    while(left != right &&  *right == v) right --;//跳过相等的元素
                }  
            }
            while(it != nums.end()-2 && *it == tmp) it++;//跳过相等的元素
        }
        return res;
    }
};
// @lc code=end

