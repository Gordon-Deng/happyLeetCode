# Weekly Contest

## Weekly Contest 276

2138.Divide a String Into Groups of Size kMy SubmissionsBack to Contest

Input: s = "abcdefghi", k = 3, fill = "x"
Output: ["abc","def","ghi"]

Input: s = "abcdefghij", k = 3, fill = "x"
Output: ["abc","def","ghi","jxx"]

```
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        
        res = []
        for i in range(0, n, k):
            if i + k <= n:
                res.append(s[i : i+k])
            else:
                res.append(s[i : n] + fill * (k - (n - i)))
        
        return res
```

2139.Minimum Moves to Reach Target Score

Input: target = 5, maxDoubles = 0
Output: 4

Input: target = 19, maxDoubles = 2
Output: 7

Input: target = 10, maxDoubles = 4
Output: 4

```
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while maxDoubles and target != 1:
            ans += 1
            if target % 2 == 1:
                target -= 1
            else:
                maxDoubles -= 1
                target //= 2
        ans += (target - 1)
        return ans
```

2140.Solving Questions With BrainpowerMy SubmissionsBack to Contest

Input: questions = [[3,2],[4,3],[4,4],[2,5]]
Output: 5

Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
Output: 7

```
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)   # 解决每道题及以后题目的最高分数
        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 1], questions[i][0] + dp[min(n, i + questions[i][1] + 1)])
        return dp[0]
```

2141.Maximum Running Time of N Computers

Input: n = 2, batteries = [3,3,3]
Output: 4

Input: n = 2, batteries = [1,1,1,1]
Output: 2


```
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l, r = 0, sum(batteries) // n
        while l < r:
            x = (l + r + 1) // 2
            if n * x <= sum(min(b, x) for b in batteries):
                l = x
            else:
                r = x - 1
        return l
```


# Biweekly Contest

### Biweekly Contest 76

```
6060. 找到最接近 0 的数字
给你一个长度为 n 的整数数组 nums ，请你返回 nums 中最 接近 0 的数字。如果有多个答案，请你返回它们中的 最大值 。

示例 1：

输入：nums = [-4,-2,1,4,8]
输出：1
解释：
-4 到 0 的距离为 |-4| = 4 。
-2 到 0 的距离为 |-2| = 2 。
1 到 0 的距离为 |1| = 1 。
4 到 0 的距离为 |4| = 4 。
8 到 0 的距离为 |8| = 8 。
所以，数组中距离 0 最近的数字为 1 。
示例 2：

输入：nums = [2,-1,1]
输出：1
解释：1 和 -1 都是距离 0 最近的数字，所以返回较大值 1 。

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return max([x if abs(x)==abs(min(nums,key=abs)) else -2e5 for x in nums])
```

```
6061. 买钢笔和铅笔的方案数
给你一个整数 total ，表示你拥有的总钱数。同时给你两个整数 cost1 和 cost2 ，分别表示一支钢笔和一支铅笔的价格。你可以花费你部分或者全部的钱，去买任意数目的两种笔。

请你返回购买钢笔和铅笔的 不同方案数目 。 

示例 1：

输入：total = 20, cost1 = 10, cost2 = 5
输出：9
解释：一支钢笔的价格为 10 ，一支铅笔的价格为 5 。
- 如果你买 0 支钢笔，那么你可以买 0 ，1 ，2 ，3 或者 4 支铅笔。
- 如果你买 1 支钢笔，那么你可以买 0 ，1 或者 2 支铅笔。
- 如果你买 2 支钢笔，那么你没法买任何铅笔。
所以买钢笔和铅笔的总方案数为 5 + 3 + 1 = 9 种。
示例 2：

输入：total = 5, cost1 = 10, cost2 = 10
输出：1
解释：钢笔和铅笔的价格都为 10 ，都比拥有的钱数多，所以你没法购买任何文具。所以只有 1 种方案：买 0 支钢笔和 0 支铅笔。

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if cost1 > total and cost2 > total :
            return 1
        big_val = max(cost1, cost2)
        small_val = min(cost1, cost2)
        
        big_n = total // big_val  # big 最多可以买的次数
        res = 0
        
        for i in range(big_n+1):
            # i 表示big买多少件
            cur_money = total - big_val * i
            small_n = cur_money // small_val
            # print(small_n+1)
            res += small_n + 1
        
        return res
```

```
6062. 设计一个 ATM 机器
一个 ATM 机器，存有 5 种面值的钞票：20 ，50 ，100 ，200 和 500 美元。初始时，ATM 机是空的。用户可以用它存或者取任意数目的钱。

取款时，机器会优先取 较大 数额的钱。

比方说，你想取 $300 ，并且机器里有 2 张 $50 的钞票，1 张 $100 的钞票和1 张 $200 的钞票，那么机器会取出 $100 和 $200 的钞票。
但是，如果你想取 $600 ，机器里有 3 张 $200 的钞票和1 张 $500 的钞票，那么取款请求会被拒绝，因为机器会先取出 $500 的钞票，然后无法取出剩余的 $100 。注意，因为有 $500 钞票的存在，机器 不能 取 $200 的钞票。
请你实现 ATM 类：

ATM() 初始化 ATM 对象。
void deposit(int[] banknotesCount) 分别存入 $20 ，$50，$100，$200 和 $500 钞票的数目。
int[] withdraw(int amount) 返回一个长度为 5 的数组，分别表示 $20 ，$50，$100 ，$200 和 $500 钞票的数目，并且更新 ATM 机里取款后钞票的剩余数量。如果无法取出指定数额的钱，请返回 [-1] （这种情况下 不 取出任何钞票）。
 

示例 1：

输入：
["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw"]
[[], [[0,0,1,2,1]], [600], [[0,1,0,1,1]], [600], [550]]
输出：
[null, null, [0,0,1,0,1], null, [-1], [0,1,0,0,1]]

解释：
ATM atm = new ATM();
atm.deposit([0,0,1,2,1]); // 存入 1 张 $100 ，2 张 $200 和 1 张 $500 的钞票。
atm.withdraw(600);        // 返回 [0,0,1,0,1] 。机器返回 1 张 $100 和 1 张 $500 的钞票。机器里剩余钞票的数量为 [0,0,0,2,0] 。
atm.deposit([0,1,0,1,1]); // 存入 1 张 $50 ，1 张 $200 和 1 张 $500 的钞票。
                          // 机器中剩余钞票数量为 [0,1,0,3,1] 。
atm.withdraw(600);        // 返回 [-1] 。机器会尝试取出 $500 的钞票，然后无法得到剩余的 $100 ，所以取款请求会被拒绝。
                          // 由于请求被拒绝，机器中钞票的数量不会发生改变。
atm.withdraw(550);        // 返回 [0,1,0,0,1] ，机器会返回 1 张 $50 的钞票和 1 张 $500 的钞票。


```