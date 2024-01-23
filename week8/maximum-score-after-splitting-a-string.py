class Solution:
    def maxScore(self, s: str) -> int:
        ans, z = 0,0
        one = s.count('1')

        for i in range(len(s) - 1):
            z += s[i] == '0'
            one -= s[i] == '1'
            ans = max(ans, z + one)

        return ans