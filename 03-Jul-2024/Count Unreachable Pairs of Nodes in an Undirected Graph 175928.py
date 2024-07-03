# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def dfs(self,i,visited,graph,done,count):
        visited.add(i)
        count=1
        done.add(i)
        for j in graph[i]:
            if j not in visited:
                count+=self.dfs(j,visited,graph,done,count)
        return count        
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph=[[] for _ in range(n)]
        for edge in edges:
            src1, des1 = edge
            src2, des2 = edge[::-1]
            graph[src1].append(des1)
            graph[src2].append(des2)
        done= set()
        b=n
        sums=0
        for i in range(n):
            if i not in done:
                visited=set()
                l=self.dfs(i,visited,graph,done,0)
                print(l)
                sums=sums+(l*(b-l))
                b=b-l
        return sums if sums>0 else 0        
                

       

        