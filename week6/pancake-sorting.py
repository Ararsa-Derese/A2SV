class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        end=len(arr)
        for i in range(len(arr)):
            idx=arr.index(max(arr[0:end]))+1
            ans.append(idx)
            ans.append(end)
            arr[0:idx]=arr[0:idx][::-1]
            arr[0:end]=arr[0:end][::-1]
            end-=1
        return ans
     


