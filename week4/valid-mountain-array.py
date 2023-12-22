class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        f=0
        for i in range(len(arr)-1):
            if i==0 and arr[i]>arr[i+1]:
                return False
            if arr[i]==arr[i+1]:
                return False
            if arr[i]>arr[i+1] and f==0:
                f=1
                continue
            if f==0 and arr[i]>arr[i+1]:
                return False
            if f==1 and arr[i]<arr[i+1]:
                return False
        if f==0:
             return False   
        return True
            
            