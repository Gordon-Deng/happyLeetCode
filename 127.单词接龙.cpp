/*
 * @lc app=leetcode.cn id=127 lang=cpp
 *
 * [127] 单词接龙
 *
 * https://leetcode-cn.com/problems/word-ladder/description/
 *
 * algorithms
 * Medium (38.78%)
 * Likes:    203
 * Dislikes: 0
 * Total Accepted:    20.5K
 * Total Submissions: 52.1K
 * Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
 *
 * 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord
 * 的最短转换序列的长度。转换需遵循如下规则：
 * 
 * 
 * 每次转换只能改变一个字母。
 * 转换过程中的中间单词必须是字典中的单词。
 * 
 * 
 * 说明:
 * 
 * 
 * 如果不存在这样的转换序列，返回 0。
 * 所有单词具有相同的长度。
 * 所有单词只由小写字母组成。
 * 字典中不存在重复的单词。
 * 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
 * 
 * 
 * 示例 1:
 * 
 * 输入:
 * beginWord = "hit",
 * endWord = "cog",
 * wordList = ["hot","dot","dog","lot","log","cog"]
 * 
 * 输出: 5
 * 
 * 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
 * ⁠    返回它的长度 5。
 * 
 * 
 * 示例 2:
 * 
 * 输入:
 * beginWord = "hit"
 * endWord = "cog"
 * wordList = ["hot","dot","dog","lot","log"]
 * 
 * 输出: 0
 * 
 * 解释: endWord "cog" 不在字典中，所以无法进行转换。
 * 
 */

// @lc code=start
// Time 68ms, 13.4MB
//BFS
//https://www.youtube.com/watch?v=vWPCm69MSfs
/*
Time Complexity: O(n*26^l) -> O(n*26^l/2), l = len(word), n=|wordList|
					bfs       双向bfs
Space Complexity: O(n)
*/
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict(wordList.begin(),wordList.end());
        if(!dict.count(endWord)){
            return 0;
        }      
        unordered_set<string> q1{beginWord};
        unordered_set<string> q2{endWord};
        int l=beginWord.size();
        int step=0;
        while(!q1.empty()&&!q2.empty()){
            step++;
            if(q1.size()>q2.size()){
                swap(q1,q2);
            }
            unordered_set<string> q;
            for(string w:q1){
                for(int i=0;i<l;i++){
                    char c=w[i];
                    for(int j='a';j<='z';j++){
                        w[i]=j;
                        if(q2.count(w)){
                            return step+1;
                        }
                        if(!dict.count(w)){
                            continue;
                        }
                        dict.erase(w);
                        q.insert(w);
                    }
                    w[i]=c;
                }
            }
            swap(q,q1);
        }
        return 0;
    }
};
// @lc code=end

