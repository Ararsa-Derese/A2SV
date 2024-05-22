# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(i, temp):
            if i == len(s):
                result.append(temp[:])
                return
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    backtrack(j, temp + [s[i:j]])
        result = []
        backtrack(0, [])
        return result