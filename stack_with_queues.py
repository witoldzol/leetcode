from collections import deque

class MyStack:
    def un_reverse(self):
        while len(self.temp):
            self.current.append(self.temp.popleft())
        self.reversed = False

    def __init__(self):
        self.size = 0
        self.current = deque()
        self.temp = deque()
        self.reversed = False
    def push(self, x: int) -> None:
        if self.reversed:
            self.un_reverse()
        self.current.append(x)
    def pop(self) -> int:
        if self.reversed:
            return self.temp.popleft()
        while len(self.current):
            i = self.current.popleft()
            if len(self.current):
                self.temp.append(i)
            else:
                self.reversed = True
                return i
    def top(self) -> int:
        if self.reversed:
            self.un_reverse()
        return self.current[0]
    def empty(self) -> bool:
        return self.size == 0

s = MyStack()
s.push(1)
s.push(2)
print(s.pop())
print(s.pop())
s.push(3)
print(s.pop())
s.push(55)
assert 55 == s.top()
