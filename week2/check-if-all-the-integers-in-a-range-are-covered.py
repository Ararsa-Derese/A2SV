class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        dic={}
        for i in range(left,right+1):
            dic[i]=0
        for i in range(left,right+1):
            for j in ranges:
               if i>=j[0] and i<=j[1]:
                   dic[i]=1
        for key,val in dic.items():
            if val==0:
                return False
        return True
