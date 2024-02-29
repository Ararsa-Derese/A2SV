class DoubleLinked:
    def __init__(self,val: str):
        self.val=val
        self.prev=None
        self.next=None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.ptr = DoubleLinked(homepage)

    def visit(self, url: str) -> None:
        temp=self.ptr
        temp.next = DoubleLinked(url)
        self.ptr=self.ptr.next
        self.ptr.prev=temp
    def back(self, steps: int) -> str:
        while self.ptr.prev and steps:
            self.ptr=self.ptr.prev
            steps-=1
        return self.ptr.val

    def forward(self, steps: int) -> str:
        while self.ptr.next and steps:
            self.ptr=self.ptr.next
            steps-=1
        return self.ptr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)