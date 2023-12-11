class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c=Counter(arr)
        for key,val in c.items():
            if val>len(arr)/4:
                return key
        return 0