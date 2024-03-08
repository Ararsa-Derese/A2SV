class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic=defaultdict(int)
        for i in range(len(intervals)):
            dic[intervals[i][0]]=i
        a=[i for i,j in intervals]
        a.sort()
        ans=[-1]*len(intervals)
        def fnd(num):
            i,j=0,len(intervals)-1
            ret=-1
            while i<=j:
                mid=(i+j)//2
                if a[mid]>=num:
                    ret=mid
                    j=mid-1
                else:
                    i=mid+1
            return ret
        for i in range(len(intervals)):
            b=fnd(intervals[i][1])
            if b!=-1:
                ans[i]=dic[a[b]]
        return ans
                

