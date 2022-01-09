# https://leetcode-cn.com/problems/a-number-after-a-double-reversal/

# int的空就为0
# 小技巧：怎么判定小数点后面是否全为零，那就是数字本身-int(数字本身)
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0 or num % 10 != 0:
            return True
        return False
