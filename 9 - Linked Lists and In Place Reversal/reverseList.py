# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        next = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous
      
# Official solution

class Solution:
    def reverseList(self, head):

        current = head
        prev = None

        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev
