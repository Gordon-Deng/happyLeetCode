#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (75.86%)
# Likes:    463
# Dislikes: 0
# Total Accepted:    58.9K
# Total Submissions: 77.2K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        n = len(nums)
        res = []

        def bfs(start, path):
            res.append(path[:])
            for i in range(start, n):
                # 这里不用i > start这么复杂，只要保证现在的数和前面不一样就行了
                if i > 0 and nums[i-1] == nums[i]:
                    continue
                path.append(nums[i])
                bfs(i+1, path)
                path.pop()

        path = []
        bfs(0, path)
        return res
# @lc code=end

