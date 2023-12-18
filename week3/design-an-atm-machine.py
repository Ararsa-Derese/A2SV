class ATM:

    def __init__(self):
        self.notes=[20,50,100,200,500]
        self.c=[0]*5
        
    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.c[i]+=banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        ans=[0]*5
        for i in range(len(self.notes)-1,-1,-1):
            a=min(amount//self.notes[i],self.c[i])
            ans[i]=a
            amount-=a*self.notes[i]
        if amount!=0:
            return [-1]
        for i in range(len(self.notes)):
            self.c[i]-=ans[i]
        return ans


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)