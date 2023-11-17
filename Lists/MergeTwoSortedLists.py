# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        if list1 and list2 is None:
            return result.next

        if list1.val <= list2.val:
            result = list1
            list1 = list1.next # becomes the next node
        else:
            result = list2
            list2 = list2.next # becomes the next node
        ref = result

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                ref.next = list1
                ref = ref.next
                list1 = list1.next
            else:
                ref.next = list2
                ref = ref.next
                list2 = list2.next
        if list1 is None:
            ref.next = list2
        else:
            ref.next = list1

        return result
