# https://leetcode-cn.com/problems/find-all-possible-recipes-from-given-supplies/

# 拓扑排序
from collections import defaultdict, deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]: 
        n = len(recipes)
        res = []
        
        #------------------- topsort
        adjvex = defaultdict(list)
        indegree = defaultdict(int)
        
        for i in range(n):
            cai = recipes[i]
            yaoqiu = ingredients[i]
            for yq in yaoqiu:
                adjvex[yq].append(cai)
                indegree[cai] += 1
        
        q = collections.deque()
        for cailiao in supplies:
            q.append(cailiao)
        while q:
            x = q.popleft()
            for y in adjvex[x]:
                indegree[y] -= 1
                if indegree[y] == 0:
                    q.append(y)
                    res.append(y)
        return res