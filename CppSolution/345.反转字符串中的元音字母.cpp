/*
 * @lc app=leetcode.cn id=345 lang=cpp
 *
 * [345] 反转字符串中的元音字母
 *
 * https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
 *
 * algorithms
 * Easy (48.53%)
 * Likes:    75
 * Dislikes: 0
 * Total Accepted:    24K
 * Total Submissions: 48.9K
 * Testcase Example:  '"hello"'
 *
 * 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
 * 
 * 示例 1:
 * 
 * 输入: "hello"
 * 输出: "holle"
 * 
 * 
 * 示例 2:
 * 
 * 输入: "leetcode"
 * 输出: "leotcede"
 * 
 * 说明:
 * 元音字母不包含字母"y"。
 * 
 */

// @lc code=start
class Solution {
private:
    bool isOrigin(char c){
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || 
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')
            return true;
        else
            return false;
    }
public:
    string reverseVowels(string s) {
        int i = 0,j = s.size();
        while(i < j){
            if(!isOrigin(s[i])){
                i++;
                continue;
            }
            if(!isOrigin(s[j])){
                j--;
                continue;
            }
            swap(s[i++],s[j--]);
        }
        return s;
    }
};
// @lc code=end

