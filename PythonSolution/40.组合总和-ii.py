#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (62.32%)
# Likes:    712
# Dislikes: 0
# Total Accepted:    205.3K
# Total Submissions: 330.1K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用一次。
# 
# 注意：解集不能包含重复的组合。 
# 
# 
# 
# 示例 1:
# 
# 
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 
# 示例 2:
# 
# 
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]
# 
# 
# 
# 提示:
# 
# 
# 1 
# 1 
# 1 
# 
# 
#

# @lc code=start
from typing import List

#  if i > start and candidates[i - 1] == candidates[i] 是如何避免重复的。
# 这个避免重复当思想是在是太重要了。
# 这个方法最重要的作用是，可以让同一层级，不出现相同的元素。即
#                   1
#                  / \
#                 2   2  这种情况不会发生 但是却允许了不同层级之间的重复即：
#                /     \
#               5       5
#                 例2
#                   1
#                  /
#                 2      这种情况确是允许的
#                /
#               2  
                
# 为何会有这种神奇的效果呢？
# 首先 cur-1 == cur 是用于判定当前元素是否和之前元素相同的语句。这个语句就能砍掉例1。
# 可是问题来了，如果把所有当前与之前一个元素相同的都砍掉，那么例二的情况也会消失。 
# 因为当第二个2出现的时候，他就和前一个2相同了。
                
# 那么如何保留例2呢？
# 那么就用cur > begin 来避免这种情况，你发现例1中的两个2是处在同一个层级上的，
# 例2的两个2是处在不同层级上的。
# 在一个for循环中，所有被遍历到的数都是属于一个层级的。我们要让一个层级中，
# 必须出现且只出现一个2，那么就放过第一个出现重复的2，但不放过后面出现的2。
# 第一个出现的2的特点就是 cur == begin. 第二个出现的2 特点是cur > begin.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        n = len(candidates)
        res = []
        def dfs(start, path, target):
            if target == 0:
                res.append(path)
                return
            for i in range(start, n):
                # 这里不能target -= candidates[i]，会被修改target的值
                residue = target - candidates[i]

                # 减枝
                if residue < 0:
                    break

                if i > start and candidates[i - 1] == candidates[i]:
                    continue

                dfs(i+1, path + [candidates[i]], residue)

        candidates.sort()
        path = []
        dfs(0, path, target)
        return res
# @lc code=end

