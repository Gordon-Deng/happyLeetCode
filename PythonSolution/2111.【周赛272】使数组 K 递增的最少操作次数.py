# https://leetcode-cn.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def find_desc_smoothly(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) == 1:	
            return True
        for i in range(len(nums)-1):
            if nums[i] - nums[i+1] !=1:
                return False
        return True

    def subsets_binary(self, nums: List[int]) -> List[List[int]]:
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
        if not prices:
            return 0
        l = self.subsets_recall(prices)
        res = 0
        for i in l:
            if self.find_desc_smoothly(i):
                print(i)
                res += 1
        return res

# 滑动窗口
    class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        res = 1   # 平滑下降阶段的总数，初值为 dp[0]
        prev = 1   # 上一个元素为结尾的平滑下降阶段的总数，初值为 dp[0]
        # 从 1 开始遍历数组，按照递推式更新 prev 以及总数 res
        for i in range(1, n):
            if prices[i] == prices[i-1] - 1:
                prev += 1
            else:
                prev = 1
            res += prev
        return res