class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        ans=[]
        while i<len(firstList) and j<len(secondList):
            if (firstList[i][0]>=secondList[j][0] and firstList[i][0]<=secondList[j][1]) or (secondList[j][0]>=firstList[i][0] and secondList[j][0]<=firstList[i][1]):
                ans.append([max(firstList[i][0],secondList[j][0]),min(firstList[i][1],secondList[j][1])])
            if firstList[i][1]>secondList[j][1]:
                j+=1
            else:
                i+=1
        return ans