class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        pre = [[0] * (m+1) for i in range(n+1)]
        ans = 0

        for i in range(1, n + 1):
            for j in range(1, m+1):
                pre[i][j] = (pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1] + matrix[i-1][j-1])

        count = 0
        for i in range(1, n+1):
            for j in range(i, n+1):
                mp = {0:1}
                for k in range(1, m+1):
                    summ = pre[j][k] - pre[i-1][k]
                    ans += mp.get(summ-target, 0)
                    mp[summ] = mp.get(summ, 0) + 1
        return ans