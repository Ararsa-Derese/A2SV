class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic={5:0,10:0,20:0}
        for b in bills:
            if b==5:
                dic[5]+=1
            elif b==10:
                if dic[5]==0:
                    return False
                else:
                    dic[5]-=1
                    dic[10]+=1
            else:
                if (dic[10]==0 and dic[5]<3) or dic[5]==0:
                    return False
                else:
                    if dic[10]==0:
                        dic[5]-=3
                        dic[20]+=1
                    else:
                        dic[10]-=1
                        dic[5]-=1
                        dic[20]+=1
        return True