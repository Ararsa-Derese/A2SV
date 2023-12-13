class UndergroundSystem:

    def __init__(self):
        self.check=defaultdict(tuple)
        self.checkO=defaultdict(tuple)
        self.avr=defaultdict(tuple)

    def checkIn(self, id, stationName, t):
       self.check[id]=(stationName, t) 
       
    def checkOut(self, id, stationName, t):
        t1=self.check[id][1]
        gap=t-t1
        if (self.check[id][0], stationName) in self.avr:
            key=(self.check[id][0], stationName)
            self.avr[key]=[self.avr[key][0]+gap,self.avr[key][1]+1]
        else:
            self.avr[(self.check[id][0], stationName)]=(gap, 1)
        
    def getAverageTime(self, startStation, endStation):
       
        return self.avr[(startStation, endStation)][0]/self.avr[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)