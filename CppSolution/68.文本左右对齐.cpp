/*
 * @lc app=leetcode.cn id=68 lang=cpp
 *
 * [68] 文本左右对齐
 *
 * https://leetcode-cn.com/problems/text-justification/description/
 *
 * algorithms
 * Hard (41.96%)
 * Likes:    46
 * Dislikes: 0
 * Total Accepted:    5.8K
 * Total Submissions: 13.8K
 * Testcase Example:  '["This", "is", "an", "example", "of", "text", "justification."]\n16'
 *
 * 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
 * 
 * 你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
 * 
 * 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
 * 
 * 文本的最后一行应为左对齐，且单词之间不插入额外的空格。
 * 
 * 说明:
 * 
 * 
 * 单词是指由非空格字符组成的字符序列。
 * 每个单词的长度大于 0，小于等于 maxWidth。
 * 输入单词数组 words 至少包含一个单词。
 * 
 * 
 * 示例:
 * 
 * 输入:
 * words = ["This", "is", "an", "example", "of", "text", "justification."]
 * maxWidth = 16
 * 输出:
 * [
 * "This    is    an",
 * "example  of text",
 * "justification.  "
 * ]
 * 
 * 
 * 示例 2:
 * 
 * 输入:
 * words = ["What","must","be","acknowledgment","shall","be"]
 * maxWidth = 16
 * 输出:
 * [
 * "What   must   be",
 * "acknowledgment  ",
 * "shall be        "
 * ]
 * 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
 * 因为最后一行应为左对齐，而不是左右两端对齐。       
 * ⁠    第二行同样为左对齐，这是因为这行只包含一个单词。
 * 
 * 
 * 示例 3:
 * 
 * 输入:
 * words =
 * ["Science","is","what","we","understand","well","enough","to","explain",
 * "to","a","computer.","Art","is","everything","else","we","do"]
 * maxWidth = 20
 * 输出:
 * [
 * "Science  is  what we",
 * ⁠ "understand      well",
 * "enough to explain to",
 * "a  computer.  Art is",
 * "everything  else  we",
 * "do                  "
 * ]
 * 
 * 
 */

// @lc code=start
class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> ret;
        string str;
        vector<int> index; // 记录每行空格的位置
        for (int i = 0; i < words.size(); i++) {
            if (str.length() + words[i].length() < maxWidth) {
                str += words[i];
                index.push_back(str.length());
                str += ' ';
            } else if (str.length() + words[i].length() == maxWidth) {
                str += words[i];
                ret.push_back(str);
                str.clear();
                index.clear();
            } else {
                int gap = maxWidth - str.length();
                if (index.size() > 1) {
                    str.erase(index.back(), 1);
                    index.pop_back();
                    gap++;
                }
                int x = 0, y = 0;
                if (!index.empty()) {
                    x = gap / index.size();
                    y = gap % index.size();
                }
                for (int j = index.size()-1; j >= 0; j--) {
                    str.insert(index[j], string(x + (j < y ? 1 : 0), ' ')); // 从后往前补齐需要的空格
                }
                ret.push_back(str);
                str = words[i];
                index.clear();
                if (str.length() < maxWidth) {
                    index.push_back(str.length());
                    str += ' ';
                }
            }
        }
        if (!str.empty()) {
            if (str.length() < maxWidth)
                str += string(maxWidth - str.length(), ' ');
            ret.push_back(str);
        }
        return ret;
    }
};
// @lc code=end

