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

```

# Biweekly Contest