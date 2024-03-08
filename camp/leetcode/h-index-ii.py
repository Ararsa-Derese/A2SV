class Solution:
    def hIndex(self, citations: List[int]) -> int:
        i,j =0,len(citations) - 1
        while i <= j:
            mid = (i + j) // 2
            if citations[mid] == len(citations) - mid:
                return len(citations) - mid
            elif citations[mid] < len(citations) - mid:
                i = mid + 1
            else:
                j = mid - 1
        return len(citations) - i
