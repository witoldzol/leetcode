from typing import Callable
from collections import deque


class Workload:
    def __init__(self, name: str, handler: Callable, dependencies: list):
        self.name = name
        self.handler = handler
        self.dependencies = dependencies or []


class DAG:
    def __init__(self) -> None:
        self.workloads = {}

    def register(self, workload: Workload) -> None:
        self.workloads[workload.name] = workload

    def run_dag(self) -> None:
        q = deque()
        no_dependencies_workloads = [
            w for _, w in self.workloads.items() if not w.dependencies
        ]
        for w in no_dependencies_workloads:
            q.append(w)
        # count deps for each workload
        how_many_deps = {name: 0 for name, _ in self.workloads.items()}

        dep_to_workload: dict[str, list[Workload]] = {}
        # build dep -> workloads map
        for _, workload in self.workloads.items():
            for dep in workload.dependencies:
                if dep in dep_to_workload:
                    dep_to_workload[dep].append(workload)
                    how_many_deps[workload.name] += 1
                else:
                    dep_to_workload[dep] = [workload]
                    how_many_deps[workload.name] += 1

        while q:
            workload = q.popleft()
            workload.handler()
            if workload.name in dep_to_workload:
                for w in dep_to_workload[workload.name]:
                    if w.name in how_many_deps:
                        how_many_deps[w.name] -= 1
                        if how_many_deps[w.name] == 0:
                            q.append(w)


def do_a():
    print("doing A work")


def do_b():
    print("doing B work")


def do_c():
    print("doing C work")


def do_d():
    print("doing D work")


d = Workload("D", do_d, ["C"])
c = Workload("C", do_c, ["B"])
a = Workload("A", do_a, [])
b = Workload("B", do_b, ["A"])
# Workload("B", do_b, [])
dag = DAG()
dag.register(a)
dag.register(b)
dag.register(c)
dag.register(d)
dag.run_dag()
