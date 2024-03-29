#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#
# https://leetcode-cn.com/problems/word-break-ii/description/
#
# algorithms
# Hard (48.90%)
# Likes:    516
# Dislikes: 0
# Total Accepted:    53.9K
# Total Submissions: 109.8K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典
# wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
# 
# 说明：
# 
# 
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 
# 
# 示例 1：
# 
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# 示例 2：
# 
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []
# 
# 
#

# @lc code=start
class Solution:
    # 超时
    @lru_cache(maxsize = None)
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        #
        wordDict = set(wordDict)

        def dfs(wordDict,temp,pos):
            #
            if pos == len(s):
                res.append(" ".join(temp))
                return
            for i in range(pos,len(s)+1):
                if s[pos:i] in wordDict:
                    temp.append(s[pos:i])
                    dfs(wordDict,temp,i)
                    temp.pop() 
        dfs(wordDict,[],0)
        return res
# @lc code=end

