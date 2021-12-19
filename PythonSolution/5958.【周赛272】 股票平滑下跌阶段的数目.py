# https://leetcode-cn.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
	def find_desc_smoothly(nums: List[str]) -> bool:

    def subsets_binary(nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for state in range(0, 1 << n):
            cur = []
            for i in range(n):
                if (state >> i) & 1:
                    cur.append(nums[i])
            res.append(cur)
        return res

    def subsets_dfs(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(idx: int, path: List[int]) -> None:
            nonlocal res
            if idx == n:
                res.append(path)
                return 
            dfs(idx + 1, path + [nums[idx]])
            dfs(idx + 1, path)

        dfs(0, [])
        return res

    def subsets_recall(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        path = []
        def backtrace(idx: int) -> None:
            nonlocal res
            nonlocal path
            if idx == n:
                res.append(path[:])
                return 
                
            backtrace(idx + 1)

            path.append(nums[idx])
            backtrace(idx + 1)
            path.pop()

        backtrace(0)
        return res

    def getDescentPeriods(self, prices: List[int]) -> int: