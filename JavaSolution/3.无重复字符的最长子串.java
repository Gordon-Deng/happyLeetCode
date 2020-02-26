/*
 * @lc app=leetcode.cn id=3 lang=java
 *
 * [3] 无重复字符的最长子串
 *
 * https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
 *
 * algorithms
 * Medium (32.44%)
 * Likes:    2984
 * Dislikes: 0
 * Total Accepted:    316.5K
 * Total Submissions: 975.2K
 * Testcase Example:  '"abcabcbb"'
 *
 * 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
 * 
 * 示例 1:
 * 
 * 输入: "abcabcbb"
 * 输出: 3 
 * 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
 * 
 * 
 * 示例 2:
 * 
 * 输入: "bbbbb"
 * 输出: 1
 * 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
 * 
 * 
 * 示例 3:
 * 
 * 输入: "pwwkew"
 * 输出: 3
 * 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
 * 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 * 
 * 
 */

// @lc code=start

// T:O(n) S:O(min(m,n))用hashmap/O(m)用table
// 滑动窗口 https://zhuanlan.zhihu.com/p/61564531
// 我们可以定义字符到索引的映射，而不是使用集合来判断一个字符是否存在。 当我们找到重复的字符时，我们可以立即跳过该窗口。
// 也就是说，如果 s[j]s[j] 在 [i, j)[i,j) 范围内有与 j'重复的字符，我们不需要逐渐增加 i 。 我们可以直接跳过 [i，j']范围内的所有元素，并将 i变为 j' + 1
class Solution {
    public int lengthOfLongestSubstring(String s) {
        // hashmap法 
        int n = s.length(), ans = 0;
        Map<Character, Integer> map = new HashMap<>(); // current index of character
        // try to extend the range [i, j]
        for (int j = 0, i = 0; j < n; j++) {
            if (map.containsKey(s.charAt(j))) {
                // abca和abcb，j'出现的位置可能比当前i大
                i = Math.max(map.get(s.charAt(j)), i);
            }
            ans = Math.max(ans, j - i + 1);
            map.put(s.charAt(j), j + 1);
        }
        return ans;
        
        // table法
        // int n = s.length(), ans = 0;
        // int[] index = new int[128]; // current index of character
        // // try to extend the range [i, j]
        // for (int j = 0, i = 0; j < n; j++) {
        //     i = Math.max(index[s.charAt(j)], i);
        //     ans = Math.max(ans, j - i + 1);
        //     index[s.charAt(j)] = j + 1;
        // }
        // return ans;
    }
}
// @lc code=end

