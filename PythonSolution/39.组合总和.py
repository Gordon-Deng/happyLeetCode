#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (72.78%)
# Likes:    1585
# Dislikes: 0
# Total Accepted:    344.2K
# Total Submissions: 473K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target
# 的唯一组合。
# 
# candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 
# 
# 对于给定的输入，保证和为 target 的唯一组合数少于 150 个。
# 
# 
# 
# 示例 1：
# 
# 
# 输入: candidates = [2,3,6,7], target = 7
# 输出: [[7],[2,2,3]]
# 
# 
# 示例 2：
# 
# 
# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]]
# 
# 示例 3：
# 
# 
# 输入: candidates = [2], target = 1
# 输出: []
# 
# 
# 示例 4：
# 
# 
# 输入: candidates = [1], target = 1
# 输出: [[1]]
# 
# 
# 示例 5：
# 
# 
# 输入: candidates = [1], target = 2
# 输出: [[1,1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# candidate 中的每个元素都是独一无二的。
# 1 
# 
# 
#

# @lc code=start
from typing import List

# 太慢了
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
                if residue < 0:
                    break
                dfs(i, path + [candidates[i]], residue)

        candidates.sort()
        path = []
        dfs(0, path, target)
        return res

# https://leetcode-cn.com/problems/combination-sum/solution/dai-ma-sui-xiang-lu-dai-ni-xue-tou-hui-s-7tum/
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         path = []
#         def backtrack(candidates,target,sum,startIndex):
#             if sum > target: return 
#             if sum == target: return res.append(path[:])
#             for i in range(startIndex,len(candidates)):
#                 if sum + candidates[i] >target: return  #如果 sum + candidates[i] > target 就终止遍历
#                 sum += candidates[i] 
#                 path.append(candidates[i])
#                 backtrack(candidates,target,sum,i)  #startIndex = i:表示可以重复读取当前的数
#                 sum -= candidates[i]  #回溯
#                 path.pop()  #回溯
#         candidates = sorted(candidates)  #需要排序
#         backtrack(candidates,target,0,0)
#         return res

if __name__ == '__main__':
    a = [2,3,6,7]
    b = 7
    test = Solution()
    print(test.combinationSum(a, b))
# @lc code=end

