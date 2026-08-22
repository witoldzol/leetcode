from collections import deque


class EventLoop:
    def __init__(self) -> None:
        self.tasks = deque()

    def create_task(self, task):
        self.tasks.append(task)

    def run(self):
        while self.tasks:
            task = self.tasks.popleft()
            try:
                if task.status == "DONE":
                    for callback in task.callbacks:
                        callback(task)
            except Exception:
                print("handling failure")
