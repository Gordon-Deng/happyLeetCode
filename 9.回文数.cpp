/*
 * @lc app=leetcode.cn id=9 lang=cpp
 *
 * [9] 回文数
 *
 * https://leetcode-cn.com/problems/palindrome-number/description/
 *
 * algorithms
 * Easy (56.87%)
 * Likes:    934
 * Dislikes: 0
 * Total Accepted:    248.9K
 * Total Submissions: 436.1K
 * Testcase Example:  '121'
 *
 * 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
 * 
 * 示例 1:
 * 
 * 输入: 121
 * 输出: true
 * 
 * 
 * 示例 2:
 * 
 * 输入: -121
 * 输出: false
 * 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
 * 
 * 
 * 示例 3:
 * 
 * 输入: 10
 * 输出: false
 * 解释: 从右向左读, 为 01 。因此它不是一个回文数。
 * 
 * 
 * 进阶:
 * 
 * 你能不将整数转为字符串来解决这个问题吗？
 * 
 */

// @lc code=start
class Solution {
public:
    bool isPalindrome(int x) {

        if (x < 0 || (x != 0 && x % 10 == 0)) // 必须有(x != 0 && x % 10 == 0) 这个条件先过滤末尾为0的数字，这种数字后续反转比较会出问题
            return false;

        int num = 0; //后半段数字的反转数字

        while (x > num)
        {
            num = num * 10 + x % 10;
            x /= 10;
        }
        
        return x == num || x == num / 10;
    }
};
// @lc code=end

