class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans=0
        c=Counter(answers)
        for key, val in c.items():
            print(key,val)
            if key==0:
                ans+=val
            elif val==key+1:
                ans+=(key+1)
            elif val%(key+1)==0:
                ans+=(key+1)*(val//(key+1))
            else:
                ans+= (key+1)*((val//(key+1))+1)
            print(ans)
        return ans 