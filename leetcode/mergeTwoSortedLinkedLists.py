# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # If list1 is None...
        if list1 is None:

            # Return list2.
            return list2

        # If list2 is None...
        if list2 is None:

            # Return list1.
            return list1

        # If the current value of list1 is the smaller one...
        if list1.val < list2.val:

            # Set the next node of list1 to a recursive call with list1.next
            # and list2.
            list1.next = self.mergeTwoLists(list1.next, list2)

            # Return list1.
            return list1

        # Else the current value of list2 is the smaller one...
        else:

            # Set the next node of list2 to a recursive call with list2.next
            # and list1.
            list2.next = self.mergeTwoLists(list1, list2.next)

            # Return list2.
            return list2
