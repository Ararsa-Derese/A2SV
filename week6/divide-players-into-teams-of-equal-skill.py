class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        prod=0
        i=0
        j=len(skill)-1
        sum=skill[0]+skill[j]
        while i<=j:
            if skill[i]+skill[j]!=sum:
                return -1
            else:
                prod+=(skill[i]*skill[j])
            i+=1
            j-=1
        
        return prod


