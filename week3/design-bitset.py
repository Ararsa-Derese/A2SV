class Bitset:

    def __init__(self, size: int):
        self.bitset=["0"]*size
        self.bitset1=["1"]*size
        self.flag=0
        self.wan=0
        self.zero=size
    def fix(self, idx: int) -> None:
        if not self.flag:
            if self.bitset[idx]!="1":
                self.bitset[idx]="1"
                self.wan+=1
                self.zero-=1
                self.bitset1[idx]="0"
            
        else:
            if self.bitset1[idx]!="1":
                self.bitset1[idx]="1"
                self.bitset[idx]="0"
                self.wan+=1
                self.zero-=1
            
    def unfix(self, idx: int) -> None:
        if not self.flag:
            if self.bitset[idx]!="0":
                self.bitset[idx]="0"
                self.wan-=1
                self.zero+=1
                self.bitset1[idx]="1"
            
        else:
            if self.bitset1[idx]!="0":
                self.bitset1[idx]="0"
                self.bitset[idx]="1"
                self.wan-=1
                self.zero+=1
    def flip(self) -> None:
        if not self.flag:
            self.flag=1
        else:
            self.flag=0
        self.wan,self.zero=self.zero,self.wan

    def all(self) -> bool:
        return self.wan==len(self.bitset)

    def one(self) -> bool:
       return self.wan>0
    def count(self) -> int:
        return self.wan

    def toString(self) -> str:
        if not self.flag:
            return ''.join(self.bitset)
        else:
            return ''.join(self.bitset1)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.wan()
# param_6 = obj.count()
# param_7 = obj.toString()