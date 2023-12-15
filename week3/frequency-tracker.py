class FrequencyTracker:

    def __init__(self):
        self.dic1={}
        self.dic2={}
    def add(self, number: int) -> None:
        if number in self.dic1:
            self.dic1[number]+=1
            if self.dic1[number] in self.dic2:
                
                self.dic2[self.dic1[number]]+=1
                if self.dic1[number]>1:
                     self.dic2[self.dic1[number]-1]-=1
            else:
                 self.dic2[self.dic1[number]]=1
                 if self.dic1[number]>1:
                     self.dic2[self.dic1[number]-1]-=1
        else:
            self.dic1[number]=1
            if self.dic1[number] in self.dic2:
                self.dic2[self.dic1[number]]+=1
            else:
                self.dic2[self.dic1[number]]=1

 
    def deleteOne(self, number: int) -> None:
        if number in self.dic1:

            if self.dic1[number] in self.dic2:
                 self.dic2[self.dic1[number]]-=1
            self.dic1[number]-=1
            if self.dic1[number] in self.dic2:
                 self.dic2[self.dic1[number]]+=1
            if self.dic1[number]==0:
                del self.dic1[number]
            

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.dic2 and self.dic2[frequency]>0:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)