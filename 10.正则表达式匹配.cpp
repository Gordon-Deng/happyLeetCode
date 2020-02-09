/*
 * @lc app=leetcode.cn id=10 lang=cpp
 *
 * [10] 正则表达式匹配
 *
 * https://leetcode-cn.com/problems/regular-expression-matching/description/
 *
 * algorithms
 * Hard (25.55%)
 * Likes:    919
 * Dislikes: 0
 * Total Accepted:    50.5K
 * Total Submissions: 194.8K
 * Testcase Example:  '"aa"\n"a"'
 *
 * 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
 * 
 * '.' 匹配任意单个字符
 * '*' 匹配零个或多个前面的那一个元素
 * 
 * 
 * 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
 * 
 * 说明:
 * 
 * 
 * s 可能为空，且只包含从 a-z 的小写字母。
 * p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
 * 
 * 
 * 示例 1:
 * 
 * 输入:
 * s = "aa"
 * p = "a"
 * 输出: false
 * 解释: "a" 无法匹配 "aa" 整个字符串。
 * 
 * 
 * 示例 2:
 * 
 * 输入:
 * s = "aa"
 * p = "a*"
 * 输出: true
 * 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
 * 
 * 
 * 示例 3:
 * 
 * 输入:
 * s = "ab"
 * p = ".*"
 * 输出: true
 * 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
 * 
 * 
 * 示例 4:
 * 
 * 输入:
 * s = "aab"
 * p = "c*a*b"
 * 输出: true
 * 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
 * 
 * 
 * 示例 5:
 * 
 * 输入:
 * s = "mississippi"
 * p = "mis*is*p*."
 * 输出: false
 * 
 */

// @lc code=start
class Solution {
    public:
    vector<vector<int>> dp;
    bool isMatch(string s, string p) {
        dp.assign(s.size()+1,vector<int>(p.size()+1,-1));
        return isMatch(s,p,0,0);
    }
    bool isMatch(string& s,string& p,int si,int pi){
        if(pi==p.size()) return si==s.size();
        if(dp[si][pi]!=-1) return dp[si][pi];
        //当si==s.size() 且 pi<p.size()时 可能p中还有“*”字符 可以令前面的字符出现0次以匹配s
        bool cur_match=false;
        if(si<s.size() && (s[si]==p[pi]||p[pi]=='.')) cur_match=true;

        if(pi+1<p.size() && p[pi+1]=='*'){  //下一个字符可能是'*'
            //当前字符可能出现0次， 或者    多次
            return dp[si][pi]=(isMatch(s,p,si,pi+2) || cur_match==true&&isMatch(s,p,si+1,pi));
        }
        return dp[si][pi]=(cur_match && isMatch(s,p,si+1,pi+1));
    }
};
// @lc code=end

