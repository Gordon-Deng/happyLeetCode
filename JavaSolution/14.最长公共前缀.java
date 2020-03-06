/*
 * @lc app=leetcode.cn id=14 lang=java
 *
 * [14] 最长公共前缀
 *
 * https://leetcode-cn.com/problems/longest-common-prefix/description/
 *
 * algorithms
 * Easy (35.72%)
 * Likes:    839
 * Dislikes: 0
 * Total Accepted:    173.5K
 * Total Submissions: 484.3K
 * Testcase Example:  '["flower","flow","flight"]'
 *
 * 编写一个函数来查找字符串数组中的最长公共前缀。
 * 
 * 如果不存在公共前缀，返回空字符串 ""。
 * 
 * 示例 1:
 * 
 * 输入: ["flower","flow","flight"]
 * 输出: "fl"
 * 
 * 
 * 示例 2:
 * 
 * 输入: ["dog","racecar","car"]
 * 输出: ""
 * 解释: 输入不存在公共前缀。
 * 
 * 
 * 说明:
 * 
 * 所有输入只包含小写字母 a-z 。
 * 
 */

// @lc code=start

// T:O(n) S:O(1)
// 神仙做法，不断用indexOf和substring去削减匹配串，如果最后还是没匹配就是没有了
// abcd abc ab
// abcd作为初始的公共前缀，与abc比较，发现不是abc的前缀，那么做减法得到abc，abc是abc的前缀，进入下一个判断，abc不是ab的前缀，减得ab ，ab是ab的前缀，遍历结束，返回ab
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0)
            return "";
        String prefix = strs[0];
        for (int i = 1; i < strs.length; i++)
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty())
                    return "";
            }
        return prefix;
    }
};
// @lc code=end

