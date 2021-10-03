#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#
# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (56.35%)
# Likes:    505
# Dislikes: 0
# Total Accepted:    74.2K
# Total Submissions: 131.6K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
# 
# 
# 
# 示例：
# 
# 输入：
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出：3
# 解释：
# 长度最长的公共子数组是 [3, 2, 1] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
# 
# 
#

# @lc code=start
# class Solution:
#     def findLength(self, nums1: List[int], nums2: List[int]) -> int:
#         # m, n = len(nums1), len(nums2)
#         # dp = [[0] * (m + 1) for _ in range(n + 1)]
#         # ans = 0

#         # for i in range(1, m+1):
#         #     for j in range(1, n1):
#         #         dp[i][j] = dp[i+1][j+1] + 1  if nums1[i] == nums2[j] else 0
#         #         ans = max(dp[i][j], ans)
#         # return ans

#         def maxLength(addA: int, addB: int, length: int) -> int:
#             ret = k = 0
#             for i in range(length):
#                 if nums1[addA + i] == nums2[addB + i]:
#                     k += 1
#                     ret = max(ret, k)
#                 else:
#                     k = 0
#             return ret
        
#         n, m = len(nums1), len(nums2)
#         ret = 0
#         for i in range(n):
#             length = min(m, n - i)
#             ret = max(ret, maxLength(i, 0, length))
#         for i in range(m):
#             length = min(n, m - i)
#             ret = max(ret, maxLength(0, i, length))
#         return ret


# DP
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # m, n = len(nums1), len(nums2)
        # dp = [[0] * (m + 1) for _ in range(n + 1)]
        # ans = 0

        # for i in range(1, m+1):
        #     for j in range(1, n1):
        #         dp[i][j] = dp[i+1][j+1] + 1  if nums1[i] == nums2[j] else 0
        #         ans = max(dp[i][j], ans)
        # return ans
        if not nums1 or not nums2:
            return 0
        sum = 0    
        len_A, len_B = len(nums1), len(nums2)
        dp = [[0] * (len_B + 1) for _ in range(len_A + 1)]
        for i in range(len_A-1, -1, -1):
            for j in range(len_B-1, -1, -1):
                dp[i][j] = dp[i+1][j+1] + 1 if nums1[i] == nums2[j] else 0
                sum = max(sum, dp[i][j])
        return sum    
# @lc code=end

