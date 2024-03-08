class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        self.dic1= defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append(value)
        self.dic1[key].append(timestamp)
    def get(self, key: str, timestamp: int) -> str:
        idx=bisect_right(self.dic1[key],timestamp)
        if idx==0:
            return ""
        return self.dic[key][idx-1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)