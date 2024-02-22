class RecentCounter:

    def __init__(self):
        self.Rc=deque()
    def ping(self, t: int) -> int:
        self.Rc.append(t)
        while t-3000 > self.Rc[0]:
            self.Rc.popleft()
        return len(self.Rc) 


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)