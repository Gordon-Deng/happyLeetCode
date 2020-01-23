/*
 * @lc app=leetcode.cn id=20 lang=cpp
 *
 * [20] 有效的括号
 *
 * https://leetcode-cn.com/problems/valid-parentheses/description/
 *
 * algorithms
 * Easy (40.44%)
 * Likes:    1334
 * Dislikes: 0
 * Total Accepted:    188.2K
 * Total Submissions: 464K
 * Testcase Example:  '"()"'
 *
 * 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
 * 
 * 有效字符串需满足：
 * 
 * 
 * 左括号必须用相同类型的右括号闭合。
 * 左括号必须以正确的顺序闭合。
 * 
 * 
 * 注意空字符串可被认为是有效字符串。
 * 
 * 示例 1:
 * 
 * 输入: "()"
 * 输出: true
 * 
 * 
 * 示例 2:
 * 
 * 输入: "()[]{}"
 * 输出: true
 * 
 * 
 * 示例 3:
 * 
 * 输入: "(]"
 * 输出: false
 * 
 * 
 * 示例 4:
 * 
 * 输入: "([)]"
 * 输出: false
 * 
 * 
 * 示例 5:
 * 
 * 输入: "{[]}"
 * 输出: true
 * 
 */

// @lc code=start
class Solution {
public:
    bool isValid(string s) {

        if (s.empty()) //注意：空字符串可被认为是有效字符串
            return true;

        if (s.size() % 2 == 1) //奇数个
            return false;

        stack<char> stack;
        
        for (int i = 0; i < s.size(); ++i)
        {
            if (s.at(i) == '(' || s.at(i) == '[' || s.at(i) == '{')
            {
                stack.push(s.at(i));
            }
            else
            {
                if (stack.empty())
                    return false;

                if ((s.at(i) == ')' && '(' != stack.top()) || (s.at(i) == ']' && '[' != stack.top()) || ((s.at(i) == '}' && '{' != stack.top())))
                    return false;

                stack.pop();
            }
        }

        return stack.empty();
    }
};
// @lc code=end

