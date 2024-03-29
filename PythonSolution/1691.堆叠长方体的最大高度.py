#
# @lc app=leetcode.cn id=1691 lang=python3
#
# [1691] 堆叠长方体的最大高度
#
# https://leetcode-cn.com/problems/maximum-height-by-stacking-cuboids/description/
#
# algorithms
# Hard (49.19%)
# Likes:    35
# Dislikes: 0
# Total Accepted:    2.6K
# Total Submissions: 5.3K
# Testcase Example:  '[[50,45,20],[95,37,53],[45,23,12]]'
#
# 给你 n 个长方体 cuboids ，其中第 i 个长方体的长宽高表示为 cuboids[i] = [widthi, lengthi,
# heighti]（下标从 0 开始）。请你从 cuboids 选出一个 子集 ，并将它们堆叠起来。
# 
# 如果 widthi j 且 lengthi j 且 heighti j ，你就可以将长方体 i 堆叠在长方体 j
# 上。你可以通过旋转把长方体的长宽高重新排列，以将它放在另一个长方体上。
# 
# 返回 堆叠长方体 cuboids 可以得到的 最大高度 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：cuboids = [[50,45,20],[95,37,53],[45,23,12]]
# 输出：190
# 解释：
# 第 1 个长方体放在底部，53x37 的一面朝下，高度为 95 。
# 第 0 个长方体放在中间，45x20 的一面朝下，高度为 50 。
# 第 2 个长方体放在上面，23x12 的一面朝下，高度为 45 。
# 总高度是 95 + 50 + 45 = 190 。
# 
# 
# 示例 2：
# 
# 
# 输入：cuboids = [[38,25,45],[76,35,3]]
# 输出：76
# 解释：
# 无法将任何长方体放在另一个上面。
# 选择第 1 个长方体然后旋转它，使 35x3 的一面朝下，其高度为 76 。
# 
# 
# 示例 3：
# 
# 
# 输入：cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
# 输出：102
# 解释：
# 重新排列长方体后，可以看到所有长方体的尺寸都相同。
# 你可以把 11x7 的一面朝下，这样它们的高度就是 17 。
# 堆叠长方体的最大高度为 6 * 17 = 102 。
# 
# 
# 
# 
# 提示：
# 
# 
# n == cuboids.length
# 1 
# 1 i, lengthi, heighti 
# 
# 
#

# @lc code=start
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)
        for i in range(n):          #本题比较简单在于，长、宽、高3个维度，要弱就都弱，不管站着、平躺、侧躺，都弱，就是真的小
            cuboids[i].sort()          #每个块从小到大排列  大的作为高
        cuboids.sort(key = lambda x: (x[2], x[1], x[0]))   #按高度，从小到大排列

        dp = [0 for _ in range(n)]
        for R in range(n):          #dp时，后面的依赖前面的，故从前往后遍历
            pre_max = 0             #跳出前面最大的情况
            for L in range(R):
                if cuboids[L][0] <= cuboids[R][0] and cuboids[L][1] <= cuboids[R][1]:   #前面的长和宽都小
                    pre_max = max(pre_max, dp[L])
            dp[R] = pre_max + cuboids[R][2]
        
        return max(dp)
# @lc code=end

