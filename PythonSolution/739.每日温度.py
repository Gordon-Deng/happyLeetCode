#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#
# https://leetcode-cn.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (67.66%)
# Likes:    860
# Dislikes: 0
# Total Accepted:    201.8K
# Total Submissions: 297.5K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 请根据每日 气温 列表 temperatures ，请计算在每一天需要等几天才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。
# 
# 示例 1:
# 
# 
# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]
# 
# 
# 示例 2:
# 
# 
# 输入: temperatures = [30,40,50,60]
# 输出: [1,1,1,0]
# 
# 
# 示例 3:
# 
# 
# 输入: temperatures = [30,60,90]
# 输出: [1,1,0]
# 
# 
# 
# 提示：
# 
# 
# 1 
# 30 
# 
# 
#

# @lc code=start

# 每一个都能成为峰值，所以stack里面不止一个原素，最后都会一一弹出来
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        l = len(T)
        stack = []    #这里定义一个栈就不用说了
        res = [0] * l   # 这里是最后要返回的result，因为题目中说没有匹配的就返回0，
                        # 所以这里初始化一个全是0的list，然后把那些有匹配的替换掉即可。

        for idx, t in enumerate(T):  # 下面是关键
            while stack and t > T[stack[-1]]:  # 当stack为空时，运行stack.append(idx)，则stack=[0]
                                                # 然后仅当遍历元素 t 小于stack顶端的值时append进去，
                                                # 这会导致stack中idx代表的元素是单调递减的，
                                                # 如果此时遍历到一个 t，大于stack顶端的值，那这个t就是离stack
                                                # 顶端值最近的那个大值。
                res[stack.pop()] = idx-stack[-1] # 然后pop出来，还是要注意stack.pop出来的是idx，这样res这
                                                 # 一串0里对应位置的0就会被替换成应有的值。                                        
                                                # 再进入while循环判断t和stack.pop后的新的顶端值哪个大。
                                                # 如此反复。
            stack.append(idx)
        return res
        
# @lc code=end

