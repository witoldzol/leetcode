# https://leetcode.com/problems/add-two-numbers/description/

# [9,9,9,9,9,9,9]
# [9,9,9,9]
# 8,9,9,9,0,0,0,1
# [8,9,9,9,0,0,0,1]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        r = []
        while True:
            if self.val:
                r.append(self.val)
            if self.next:
                self = self.next
            else:
                break
        return str(r)

# def test_array_to_linked_list():
#     ll = Solution().array_to_linked_list([1,2,3])
#     print("==================================================")
#     print(f"{ll=}")
#     print("==================================================")
#     result = []
#     while True:
#         result.append(ll.val)
#         if ll.next:
#             ll = ll.next
#         else:
#             break
#     assert result == [1,2,3]

from typing import Optional, List

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

import pudb
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # pu.db
        result = []
        carry_over = 0
        end = 0
        l1_end = False
        l2_end = False
        while True:
            if l1_end and l2_end:
                break
            if l1 and l1.val:
                l = l1.val
                l1 = l1.next
            else:
                l = 0
                l1_end = True
            if l2 and l2.val:
                r = l2.val
                l2 = l2.next
            else:
                r = 0
                l2_end = True
            sum = l + r + carry_over
            if sum > 9:
                carry_over = sum // 10
                end = sum % 10
                result.append(end)
            else:
                result.append(sum)
                carry_over = 0
        if carry_over > 0:
            reminder = ''.split(str(carry_over))
            if len(reminder) == 1 and reminder[0] == '':
                return array_to_linked_list(result)
            result.append(reminder)
        return array_to_linked_list(result)

 # l1 = array_to_linked_list([1,2,3])
# l2 = array_to_linked_list([1,2,3])
# print(Solution().addTwoNumbers(l1,l2))

l = array_to_linked_list([9,9,9,9,9,9,9])
r = array_to_linked_list([9,9,9,9])
# [8,9,9,9,0,0,0,1]
s = Solution().addTwoNumbers(l,l)
print("==================================================")
print("==================================================")
print(f"result is = {s} and it should be [8,9,9,9,0,0,0,1]")
print("==================================================")
print("==================================================")
assert [8,9,9,9,0,0,0,1] == s
