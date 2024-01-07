class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        ans = 0
        r = 0
        j = 0
        i=0
        while i<len(s):
            j = i - 1
            while j >= r:
                if s[j] == s[i]:
                    i = j + 1
                    r = i
                    if ans < count:
                        ans = count
                    count = 0
                j -= 1
            count += 1
            i+=1
        if count > ans:
            return count
        else:
            return ans