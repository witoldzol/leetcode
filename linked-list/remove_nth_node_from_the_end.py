# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from util import ListNode, ll_to_array, array_to_linked_list
from typing import List, Optional

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
# go to the end - get len
# len - n - 1 node.next = node.next.next # done
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    node_before_node_to_be_deleted = length - n - 1
    curr = head
    for _ in range(node_before_node_to_be_deleted):
        curr = curr.next
    # delete the target node
    curr.next = curr.next.next
    return head

h = array_to_linked_list([1,2,3])
result = removeNthFromEnd(h, 2)
assert [1,3] == ll_to_array(result)

h = array_to_linked_list([1,2,3,4,5])
result = removeNthFromEnd(h, 2)
assert [1,2,3,5] == ll_to_array(result)
# print(f"{result=}")

