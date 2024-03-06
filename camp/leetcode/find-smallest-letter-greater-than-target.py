class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans=letters[0]
        i,j=0,len(letters)-1
        while i<=j:
            mid=(i+j)//2
            if ord(letters[mid])>ord(target):
                j=mid-1
                ans=letters[mid]
            else:
                i=mid+1
        return ans