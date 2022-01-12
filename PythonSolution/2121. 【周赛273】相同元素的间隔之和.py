# https://leetcode-cn.com/problems/intervals-between-identical-elements/

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        position_dict = defaultdict(list)
        for i in range(len(arr)):
            position_dict[arr[i]].append(i)

        ans = [0] * len(arr)
        for _, value in position_dict.items():
            n = len(value)
            ans[value[0]] = sum([value[i] - value[0] for i in range(1, len(value))])
            for i in range(1, len(value)):
                ans[value[i]] = ans[value[i-1]] + (i - 1) * (value[i] - value[i-1]) - (n - i - 1) * (value[i] - value[i-1])
        return ans