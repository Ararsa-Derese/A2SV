class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        ans=""
        if len(palindrome)==1:
            return ""
        c=palindrome.count('a')
        if palindrome[0]!='a':
            return "a"+palindrome[1:]
        for i in range(len(palindrome)):
            if palindrome[i]!="a":
                if palindrome[i-1:i]=="a" and palindrome[i+1:i+2]=="a":
                    continue
                else:
                    ans=palindrome[:i]+"a"+palindrome[i+1:]
                    return ans
            elif i!=0 and palindrome[i]=="a" and c==1:
                ans=palindrome[:i]+"b"+palindrome[i+1:]
                return ans
            else:
                c-=1
        return ans