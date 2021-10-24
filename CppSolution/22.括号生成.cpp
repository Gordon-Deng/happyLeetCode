/*
 * @lc app=leetcode.cn id=22 lang=cpp
 *
 * [22] 括号生成
 *
 * https://leetcode-cn.com/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (72.75%)
 * Likes:    758
 * Dislikes: 0
 * Total Accepted:    75.3K
 * Total Submissions: 102.7K
 * Testcase Example:  '3'
 *
 * 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
 * 
 * 例如，给出 n = 3，生成结果为：
 * 
 * [
 * ⁠ "((()))",
 * ⁠ "(()())",
 * ⁠ "(())()",
 * ⁠ "()(())",
 * ⁠ "()()()"
 * ]
 * 
 * 
 */

// @lc code=start

// T:O() S:O()
// 此题我们要保证生成的括号字符串合法。
// 我们用l，r分别记录可以插入 '(' 和 ')' 的数量。
// 例如n = 3，那么一开始r = 0，l = 3。
// 当我们在递归函数中，选择插入 '(' 时，l要 - 1，r要 + 1。
// 因为你插入你一个'('势必要在接下来插入一个')'。
// 当我们在递归函数中，选择插入 ')' 时，r只需- 1即可
class Solution {
public:
    void getAns(string str, int l, int r, vector<string>& ans){
        if(l == 0 && r == 0)
            ans.push_back(str);
        if(l > 0)
            getAns(str + "(", l - 1, r + 1, ans);
        if(r > 0) 
           getAns(str + ")", l, r - 1, ans);
    }
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        getAns("", n, 0, ans);
        return ans;
    }
};
// @lc code=end
