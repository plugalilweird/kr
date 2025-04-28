class Solution:
    def isTree(self, n, m, edges):
        if n - 1 != m:
            return 0
        dict1 = {i: [] for i in range(n)}
        for i,j in edges:
            if i == j:
                return 0
            if j in dict1[i]:
                return 0
            dict1[i].append(j)
            dict1[j].append(i)
        dfs=[]
        path=[]
        check= [0] * n
        def dfs_util(u):
            check[u]=1
            path.append(u)
            for v in dict1[u]:
                if v in path[:-2]:
                    return 0
                if not check[v]:
                    if not dfs_util(v):
                        return 0
            path.pop()
            return 1
        if dfs_util(0) and all(check):
            return 1
        return 0