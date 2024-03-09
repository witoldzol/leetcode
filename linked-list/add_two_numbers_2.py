# https://leetcode.com/problems/add-two-numbers/description/
from typing import Optional, List
# import pudb


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


def ll_to_array(head: ListNode) -> List[int]:
    curr = head
    while curr:
        yield curr.val
        curr = curr.next


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


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = []
        carry_over = 0
        end = 0
        l1_end = False
        l2_end = False
        while True:
            if l1:
                l = l1.val
                l1 = l1.next
            else:
                l = 0
                l1_end = True
            if l2:
                r = l2.val
                l2 = l2.next
            else:
                r = 0
                l2_end = True
            if l1_end and l2_end and carry_over == 0:
                break
            sum = l + r + carry_over
            if sum > 9:
                carry_over = sum // 10
                end = sum % 10
                result.append(end)
                print(f"{result=}")
            else:
                result.append(sum)
                carry_over = 0
        if carry_over > 0:
            reminder = "".split(str(carry_over))
            if len(reminder) == 1 and reminder[0] == "":
                return array_to_linked_list(result)
            result.append(reminder)
        return array_to_linked_list(result)

l = array_to_linked_list([2, 4, 3])
r = array_to_linked_list([5, 6, 4])
s = Solution().addTwoNumbers(l, r)
r = list(ll_to_array(s))
assert r == [7, 0, 8]
def test_foo():
    l = array_to_linked_list([9, 9, 9, 9, 9, 9, 9])
    r = array_to_linked_list([9, 9, 9, 9])
    s = Solution().addTwoNumbers(l, r)
    r = list(ll_to_array(s))
    assert r == [8, 9, 9, 9, 0, 0, 0, 1]
    l = array_to_linked_list([2, 4, 3])
    r = array_to_linked_list([5, 6, 4])
    s = Solution().addTwoNumbers(l, r)
    r = list(ll_to_array(s))
    assert r == [7, 0, 8]
    l = array_to_linked_list([0])
    r = array_to_linked_list([0])
    s = Solution().addTwoNumbers(l, r)
    r = list(ll_to_array(s))
    assert r == [0]
