/*
 * @lc app=leetcode.cn id=557 lang=cpp
 *
 * [557] 反转字符串中的单词 III
 *
 * https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/description/
 *
 * algorithms
 * Easy (68.74%)
 * Likes:    154
 * Dislikes: 0
 * Total Accepted:    41.4K
 * Total Submissions: 59.8K
 * Testcase Example:  `"Let's take LeetCode contest"`
 *
 * 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
 * 
 * 示例 1:
 * 
 * 
 * 输入: "Let's take LeetCode contest"
 * 输出: "s'teL ekat edoCteeL tsetnoc" 
 * 
 * 
 * 注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
 * 
 */

// @lc code=start
class Solution {
public:
    // 反转字符串
    void reverseString(int front, int tail, string& str) {
        while (front < tail) {
            str[front] ^= str[tail];
            str[tail] ^= str[front];
            str[front++] ^= str[tail--];
        }
    }
    // 确定单词边界
    string reverseWords(string s) {
        int front = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == ' ') {
                reverseString(front, i - 1, s);
                front = i + 1;
            }
        }
        reverseString(front, s.length() - 1, s);
        return s;
    }
};
// @lc code=end

