# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Store the previous and current Nodes.
        prevNode = None
        currNode = head

        # While we have a current Node.
        while currNode:
            
            # Store the rest of the list in a temp Node.
            tempNode = currNode.next
            
            # Set the curret Node's next to the previous Node.
            currNode.next = prevNode
            
            # Set the new previous Node to the current Node.
            prevNode = currNode
            
            # Make the new current Node the temp Node from earlier.
            currNode = tempNode

        # Return the previous Node which is now the new head.
        return prevNode
