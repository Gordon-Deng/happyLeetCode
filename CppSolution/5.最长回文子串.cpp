/*
 * @lc app=leetcode.cn id=5 lang=cpp
 *
 * [5] 最长回文子串
 *
 * https://leetcode-cn.com/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (28.04%)
 * Likes:    1622
 * Dislikes: 0
 * Total Accepted:    165.2K
 * Total Submissions: 588K
 * Testcase Example:  '"babad"'
 *
 * 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
 * 
 * 示例 1：
 * 
 * 输入: "babad"
 * 输出: "bab"
 * 注意: "aba" 也是一个有效答案。
 * 
 * 
 * 示例 2：
 * 
 * 输入: "cbbd"
 * 输出: "bb"
 * 
 * 
 */

// @lc code=start
class Solution {
public:
    string longestPalindrome(string s){
	int len = s.length();
	if (len < 1)
	{
		return "";
	}

	// 预处理
	string s1;
	for (int i = 0; i < len; i++)
	{
		s1 += "#";
		s1 += s[i];
	}
	s1 += "#";

	len = s1.length();
	int MaxRight = 0;				// 当前访问到的所有回文子串，所能触及的最右一个字符的位置
	int pos = 0;					// MaxRight对应的回文串的对称轴所在的位置
	int MaxRL = 0;					// 最大回文串的回文半径
	int MaxPos = 0;					// MaxRL对应的回文串的对称轴所在的位置
	int* RL = new int[len];			// RL[i]表示以第i个字符为对称轴的回文串的回文半径
	memset(RL, 0, len * sizeof(int));
	for (int i = 0; i < len; i++)
	{
		if (i < MaxRight)
		{// 1) 当i在MaxRight的左边
			RL[i] = min(RL[2 * pos - i], MaxRight - i);
		}
		else
		{// 2) 当i在MaxRight的右边
			RL[i] = 1;
		}


		// 尝试扩展RL[i]，注意处理边界
		while (i - RL[i] >= 0  // 可以把RL[i]理解为左半径,即回文串的起始位不能小于0
			&& i + RL[i] < len // 同上,即回文串的结束位不能大于总长
			&& s1[i - RL[i]] == s1[i + RL[i]]// 回文串特性，左右扩展，判断字符串是否相同
			)
		{
			RL[i] += 1;
		}

		// 更新MaxRight, pos
		if (RL[i] + i - 1 > MaxRight)
		{
			MaxRight = RL[i] + i - 1;
			pos = i;
		}

		// 更新MaxRL, MaxPos
		if (MaxRL <= RL[i])
		{
			MaxRL = RL[i];
			MaxPos = i;
		}
	}
	return s.substr((MaxPos - MaxRL + 1) / 2, MaxRL - 1);
    }
};
// @lc code=end

