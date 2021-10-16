#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (58.24%)
# Likes:    350
# Dislikes: 0
# Total Accepted:    59.1K
# Total Submissions: 96.2K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        n = len(nums)
        res = []

        def bfs(start, path):
            res.append(path[:])
            for i in range(start, n):
                # 这里不用i > start这么复杂，只要保证现在的数和前面不一样就行了
                if nums[i-1] == nums[i]:
                    continue
                path.append(nums[i])
                bfs(i+1, path)
                path.pop()
        nums.sort()
        path = []
        bfs(0, path)
        return res
# @lc code=end

