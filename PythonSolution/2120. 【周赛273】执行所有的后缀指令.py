# https://leetcode-cn.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        ans = list()
        for i in range(m):
            x, y = startPos
            cnt = m - i
            for j in range(i, m):
                ch = s[j]
                if ch == "L":
                    y -= 1
                elif ch == "R":
                    y += 1
                elif ch == "U":
                    x -= 1
                else:
                    x += 1
                if x < 0 or x >= n or y < 0 or y >= n:
                    cnt = j - i
                    break
            ans.append(cnt)
        return ans