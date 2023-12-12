class OrderedStream:

    def __init__(self, n: int):
        self.li=[[] for i in range(n+1)]
        self.pt=1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.li[idKey]=value
        ans=[]
        if idKey==self.pt:
            ans.append(value)
            self.pt+=1
            while self.pt<len(self.li) and len(self.li[self.pt])>0:
                 ans.append(self.li[self.pt])
                 self.pt+=1
        return ans



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)