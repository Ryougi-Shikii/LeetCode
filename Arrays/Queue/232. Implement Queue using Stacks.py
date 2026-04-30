class MyQueue:

    def __init__(self):
        self.pushq = []
        self.popq = []

    def push(self, x: int) -> None:
        self.pushq.append(x)

    def pop(self) -> int:
        self.shifting()
        return self.popq.pop()

    def peek(self) -> int:
        self.shifting()
        return self.popq[-1]

    def empty(self) -> bool:
        return not self.pushq and not self.popq
    
    def shifting(self):
        if not self.popq:
            while self.pushq:
                self.popq.append(self.pushq.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()