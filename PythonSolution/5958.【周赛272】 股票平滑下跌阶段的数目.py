# https://leetcode-cn.com/problems/number-of-smooth-descent-periods-of-a-stock/

    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = list()

        ptr = 0
        for i, ch in enumerate(s):
            if ptr < len(spaces) and spaces[ptr] == i:
                ans.append(" ")
                ptr += 1
            ans.append(ch)
        
        return "".join(ans)