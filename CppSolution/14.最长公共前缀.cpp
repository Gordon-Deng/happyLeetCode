/*
 * @lc app=leetcode.cn id=14 lang=cpp
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
class Solution {
public:
   string longestCommonPrefix(vector<string>& strs) {
		if (strs.size() == 0) return "";//strs无字符串，则为空
		string prefix = strs[0];//假设第一个字符串为公共前缀
		for (int i=1;i<strs.size();i++)//判断每一个字符串中是否含有prefix，
		{
			while (strs[i].find(prefix)!=0)//如果不含有prefix，则将prefix长度减1，再次判断prefix-1是否为其子串（==0表示含有该字串），直到prefix为空，
			{
				if (prefix == "") return "";//如果prefix为空串，则说明公共前缀为空
				prefix = prefix.substr(0, prefix.length() - 1);
			}
		}
		return prefix;
	}
};
// @lc code=end

