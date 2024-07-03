# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        parent = [i for i in range(n+1)]
    
        rank = [0 for i in range(n+1)]

        def find(parent, x):

            if parent[x] == x:
                return x
            parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, a, b):

            a = find(parent, a)
            b = find(parent, b)

            if a == b:
                return 

            if rank[a] < rank[b]:
                parent[a] = b
            elif rank[a] > rank[b]:
                parent[b] = a
            else:
                parent[b] = a
                rank[a] += 1
                
        edgeList.sort(key = lambda x: x[2])
        res = [0] * len(queries)
        queries = [[i, ch] for i, ch in enumerate(queries)]
        queries.sort(key = lambda x: x[1][2])
        
        ind = 0
        for i, (a, b, w) in queries:
            
            while ind < len(edgeList) and edgeList[ind][2] < w:
                union(parent, edgeList[ind][0], edgeList[ind][1])
                ind += 1
                
            res[i] = find(parent, a) == find(parent, b)
        return res