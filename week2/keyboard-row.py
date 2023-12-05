class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1="qwertyuiop"
        r2="asdfghjklasdfghjkl"
        r3="zxcvbnm"
        ans=[]
        dic={1:r1,2:r2,3:r3}
        r=1
        for i in words:
            if i[0].lower() in r1:
                r=1
            elif i[0].lower() in r2:
                r=2
            else:
                r=3
            for j in range(1,len(i)):
                if i[j].lower() not in dic[r]:
                    break
            else:
                ans.append(i)
        return ans
                