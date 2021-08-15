#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# https://leetcode-cn.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (49.58%)
# Likes:    1123
# Dislikes: 0
# Total Accepted:    177K
# Total Submissions: 356.9K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
# 
# 返回滑动窗口中的最大值。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1], k = 1
# 输出：[1]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1,-1], k = 1
# 输出：[1,-1]
# 
# 
# 示例 4：
# 
# 
# 输入：nums = [9,11], k = 2
# 输出：[11]
# 
# 
# 示例 5：
# 
# 
# 输入：nums = [4,-2], k = 2
# 输出：[4]
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10^4 
# 1 
# 
# 
#

# @lc code=start

# heapq.heapify(q)堆的操作
# 原理有点拗口，就是每次维护一个大顶堆，注意不要被窗口大小限制思想，这道题不用理固定堆的大小就为K，只需要看堆顶的最大值是否在当前窗口即可
# 当滑动窗口移动时，若最大值不在窗口，那就弹出去，否则一值滑动一直往堆里加元素就好了
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        
        return ans
# @lc code=end

