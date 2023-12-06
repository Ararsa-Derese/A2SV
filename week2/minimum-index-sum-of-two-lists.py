class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic=defaultdict(list)
        ans=[]
        for l in list1:
            if l in list2:
                dic[list1.index(l)+list2.index(l)].append(l)
      
        for j in dic:
            
            if j==min(dic.keys()):
                for i in dic[j]:
                    ans.append(i)
        return ans