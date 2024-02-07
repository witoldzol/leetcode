from collections import deque

class MyStack:
    def __init__(self):
        self.size = 0
        self.current = deque()
        self.temp = deque()
    def push(self, x: int) -> None:
        self.current.append(x)
    def pop(self) -> int:
        pass
    def top(self) -> int:
        pass
    def empty(self) -> bool:
        return self.size == 0


# LIFO from two FIFO
# push 1,2,3
# queue(1,2,4)
# move to second 
# second (1,2) - check if last item ( in temp ), don't push to second queue, just return
# pop -> 3
# push 4
# pop -> 4
