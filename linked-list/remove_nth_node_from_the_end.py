# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from util import ListNode, ll_to_array, array_to_linked_list
from typing import List, Optional

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
# go to the end - get len
# len - n - 1 node.next = node.next.next # done
    length = 0
    curr = head
    # calc len
    while curr:
        length += 1
        curr = curr.next
    # edge case
    if length == n:
        head = head.next
        return head
    node_before_node_to_be_deleted = length - n - 1
    curr = head
    for _ in range(node_before_node_to_be_deleted):
        curr = curr.next
    # delete the target node
    curr.next = curr.next.next
    return head

def test_bob():
    h = array_to_linked_list([1,2,3])
    result = removeNthFromEnd(h, 2)
    expected = [1,3]
    assert expected == ll_to_array(result)

    h = array_to_linked_list([1,2,3,4,5])
    result = removeNthFromEnd(h, 2)
    expected = [1,2,3,5]
    assert expected == ll_to_array(result)

    h = array_to_linked_list([1,2])
    result = removeNthFromEnd(h, 2)
    expected = [2]
    assert expected == ll_to_array(result)
