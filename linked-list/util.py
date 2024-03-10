from typing import List, Generator

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        r = []
        while True:
            if self.val != None:
                r.append(self.val)
            if self.next:
                self = self.next
            else:
                break
        return str(r)


def ll_to_array_generator(head: ListNode) -> Generator[int, None, None]:
    curr = head
    while curr:
        yield curr.val
        curr = curr.next

def ll_to_array(head: ListNode) -> List[int]:
    return list(ll_to_array_generator(head))

def array_to_linked_list(arr: List[int]) -> ListNode | None:
    head = None
    tail = None
    for x in arr:
        if head == None:
            head = ListNode(x)
            tail = head
        else:
            tail.next = ListNode(x)
            tail = tail.next
    return head

