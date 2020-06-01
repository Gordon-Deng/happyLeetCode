/*
 * @lc app=leetcode.cn id=125 lang=java
 *
 * [125] 验证回文串
 *
 * https://leetcode-cn.com/problems/valid-palindrome/description/
 *
 * algorithms
 * Easy (41.93%)
 * Likes:    151
 * Dislikes: 0
 * Total Accepted:    75.4K
 * Total Submissions: 178.6K
 * Testcase Example:  '"A man, a plan, a canal: Panama"'
 *
 * 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
 * 
 * 说明：本题中，我们将空字符串定义为有效的回文串。
 * 
 * 示例 1:
 * 
 * 输入: "A man, a plan, a canal: Panama"
 * 输出: true
 * 
 * 
 * 示例 2:
 * 
 * 输入: "race a car"
 * 输出: false
 * 
 * 
 */

// @lc code=start

// T:O(n) S:O(1)
class Solution {
    public boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        char[] charArray = s.toCharArray();
        while (i < j) {
            // 将i和j指向第一个是字母和数字的位置
            while (!Character.isLetterOrDigit(charArray[i]) && i < j) {
                i++;
            }
            while (!Character.isLetterOrDigit(charArray[j]) && i < j) {
                j--;
            }

            // 如果不相等，就返回false
            if ((int) Character.toLowerCase(charArray[i]) != (int) Character.toLowerCase(charArray[j])) {
                return false;
            }

            // 将i和j向中间移动
            i++;
            j--;
        }
        return true;
    }
}
// @lc code=end
