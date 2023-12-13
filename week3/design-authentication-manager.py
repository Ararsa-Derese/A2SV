class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.dic={}
        self.tm=timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.dic[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        t = currentTime-self.tm       
        if tokenId in self.dic and self.dic[tokenId]>t:  
            self.dic[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        limit = currentTime-self.tm      
        c = 0
        for i in self.dic:
            if self.dic[i]>limit:         
                c+=1
        return c


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)