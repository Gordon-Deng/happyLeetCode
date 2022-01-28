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



# Biweekly Contest