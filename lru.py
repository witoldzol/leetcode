# 1:1, 2:2, get(1) 
class Node():
    def __init__(self, key, val) -> None:
        self.next = self.prev = None
        self.key = key
        self.val = val

    def __repr__(self):
        return f"Node(key={self.key},val={self.val})"

class LRUCache():
    def __init__(self, capacity: int) -> None:
        self.cache: dict[int, Node] = {}
        self.capacity = capacity
        self.lru = Node(None,None)
        self.mru = Node(None,None)

    def remove_from_queue(self, node:Node) -> None:
        print(f'removing node {node}')
        # if node is in the 'middle'
        if node.prev:
            # prev -> node_to_remove -> next
            # prev -> next
            node.prev.next = node.next
            if node.next:
                # prev <- next
                node.next.prev = node.prev
                # no changes to mru, lru because node is not on the 'edge'
            else:
                # prev -> node_to_remove -> None
                # removed node was at the 'end' of queue
                self.mru = node.prev
        else:
            # None -> node_to_remove -> next
            # None <- c
            if node.next:
                node.next.prev = None
                self.lru = node.next
            else:
                # None > node to remove > None
                self.queue = None
                self.lru = None
                self.mru = None

    def print_queue(self) -> None:
        queue = []
        if self.mru:
            curr = self.mru
            while curr:
                queue.append(curr)
                curr = curr.next
        return queue

    def add_to_queue(self, node:Node) -> None:
        if self.mru:
            self.mru.prev = node
            node.next = self.mru
            self.mru = node
        else:
            # empty queue
            self.mru = node
            self.lru = node
        print(f"Current queue: {self.print_queue()}")

    def get(self, key:int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        if self.mru != node:
            self.remove_from_queue(node)
            self.add_to_queue(node)
        return node.val

    def put(self, key:int, value:int) -> None:
        # existing key
        if key in self.cache:
            node = self.cache[key]
            if self.mru == node:
                # inserted node is already mru, no need to do anything
                pass
            else:
                self.remove_from_queue(node)
                self.add_to_queue(node)
            # remove key from queue ( unless mru )
            # add key to queue
        # new key
        else:
            node = Node(key, value)
            self.cache[key] = node
            # check capacity
            if len(self.cache) >= self.capacity:
                self.remove_from_queue(self.lru)
            self.add_to_queue(node)


op = ["put","put"]
input = [[1,1],[2,2]]
# op = ["put","put","get","put","get","put","get","get","get"]
# input = [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

lru = LRUCache(2)
z = zip(op,input)
for x in z:
    op = x[0]
    i = x[1]
    if op == 'put':
        lru.put(i[0],i[1])
    else:
        lru.get(i[0])
    print('op ', op,' input ', i, ' current cache ', lru.cache)
