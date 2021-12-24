# https://leetcode-cn.com/problems/minimum-operations-to-make-the-array-k-increasing/


# DP
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)
        ans = 0
        for i in range(k):
            f = list()
            j, length = i, 0
            while j < n:
                length += 1
                it = bisect_right(f, arr[j])
                if it == len(f):
                    f.append(arr[j])
                else:
                    f[it] = arr[j]
                j += k
            ans += length - len(f)
        return ans