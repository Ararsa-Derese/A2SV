class Solution:
    def decodeString(self, s: str) -> str:
        def dec(i,s):
            num=""
            a=""
            while i<len(s):
                if s[i].isdigit():
                    num+=s[i]
                    i+=1
                    continue
                elif s[i]=="[":
                    val,i,s=dec(i+1,s)
                    a+=(int(num)*val)
                    num=""
                    i+=1
                    continue
                elif s[i]=="]":
                    return a,i,s
                a+=s[i]
                i+=1
            return a,i,s
        i=0        
        return dec(i,s)[0]