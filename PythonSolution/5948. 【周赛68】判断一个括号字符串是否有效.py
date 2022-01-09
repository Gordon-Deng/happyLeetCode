# https://leetcode-cn.com/problems/check-if-a-parentheses-string-can-be-valid/

# 模拟
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n %2 != 0:
            return False
        stack_left = []
        stack_any = []
        for i in range(len(s)):
            if locked[i] == '0':
                stack_any.append(i)
            else: #locked
                if s[i] == ')': 
                    if stack_left and stack_left[-1] < i:
                        stack_left.pop()
                    elif stack_any and stack_any[-1] < i:
                        stack_any.pop()
                    else:
                        return False
                else:
                    stack_left.append(i)
        print(stack_left)
        while stack_left:
            if stack_any and stack_any[-1] > stack_left[-1]:
                stack_any.pop()
                stack_left.pop()
            else:
                return False

        return len(stack_left) == 0