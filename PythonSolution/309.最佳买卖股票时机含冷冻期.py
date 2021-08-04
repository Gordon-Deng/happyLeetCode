#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (59.56%)
# Likes:    832
# Dislikes: 0
# Total Accepted:    101.3K
# Total Submissions: 169.2K
# Testcase Example:  '[1,2,3,0,2]'
#
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
# 
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 
# 
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 
# 
# 示例:
# 
# 输入: [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
# 
#

# @lc code=start
# T:O(N) S:O(N)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 1:#无法交易
            return 0
        #按照第二天(prices[1])的股票价格确定初始状态
        buy =-min(prices[0],prices[1]) #手头持有,最大的收益即为 0-最小价格
        sell = prices[1]-prices[0] #当日卖出, 收益固定为prices[1] - prices[0]
        hold = 0 #当日不进行操作且手头无股票, 收益为0

        #从第三天开始
        for price in prices[2:]:

            buy, sell, hold = max(buy, hold - price), price + buy, max(hold, sell)
            #1.若当日持有, 最大受益为 max(上日hold今日买入, 继续持有上日持有的股票)
            #2.若当日卖出, 收益固定为当日价格减去上日的成本
            #当日不操作且收头无股票, 最大受益为 max(上日hold 今日仍hold, 上日卖出今日hold)

        return max(sell, hold)
# @lc code=end

