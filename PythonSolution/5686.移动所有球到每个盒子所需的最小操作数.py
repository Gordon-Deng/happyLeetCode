#
# @lc app=leetcode.cn id=5686 lang=python3
#
# [5686] 移动所有球到每个盒子所需的最小操作数
#
# https://leetcode-cn.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/
#
# algorithms
# Medium (92.63%)
# Likes:    5
# Dislikes: 0
# Total Accepted:    3K
# Total Submissions: 3.2K
# Testcase Example:  '"110"'
#
# 有 n 个盒子。给你一个长度为 n 的二进制字符串 boxes ，其中 boxes[i] 的值为 '0' 表示第 i 个盒子是 空 的，而
# boxes[i] 的值为 '1' 表示盒子里有 一个 小球。
# 
# 在一步操作中，你可以将 一个 小球从某个盒子移动到一个与之相邻的盒子中。第 i 个盒子和第 j 个盒子相邻需满足 abs(i - j) == 1
# 。注意，操作执行后，某些盒子中可能会存在不止一个小球。
# 
# 返回一个长度为 n 的数组 answer ，其中 answer[i] 是将所有小球移动到第 i 个盒子所需的 最小 操作数。
# 
# 每个 answer[i] 都需要根据盒子的 初始状态 进行计算。
# 
# 
# 
# 示例 1：
# 
# 输入：boxes = "110"
# 输出：[1,1,3]
# 解释：每个盒子对应的最小操作数如下：
# 1) 第 1 个盒子：将一个小球从第 2 个盒子移动到第 1 个盒子，需要 1 步操作。
# 2) 第 2 个盒子：将一个小球从第 1 个盒子移动到第 2 个盒子，需要 1 步操作。
# 3) 第 3 个盒子：将一个小球从第 1 个盒子移动到第 3 个盒子，需要 2 步操作。将一个小球从第 2 个盒子移动到第 3 个盒子，需要 1
# 步操作。共计 3 步操作。
# 
# 
# 示例 2：
# 
# 输入：boxes = "001011"
# 输出：[11,8,5,4,3,4]
# 
# 
# 
# 提示：
# 
# 
# n == boxes.length
# 1 <= n <= 2000
# boxes[i] 为 '0' 或 '1'
# 
# 
#

# @lc code=start
# @Author: Gordon Deng;
# @Date: 2021-02-21 20:06:56

# abs(i - j)意思为取绝对值

# 动态规划：
# 下一个盒子所需要的操作数，可以根据前一个盒子的操作数得到
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        dp = [0] * len(boxes)
        right = 0
        for i in range(len(boxes)):
            if boxes[i] == '1' : 
               dp[0] += i
               right += 1
        left = 0
        for j in range(1, len(boxes)):
            if boxes[j-1] == '1' :
                left += 1
                right -= 1
            dp[j] = dp[j-1] - right + left
        return dp
# @lc code=end

