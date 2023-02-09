# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next: return head
        first = head
        second = head.next
        odd = first
        even = second
        while odd and even:
            odd.next = even.next
            if not odd.next:
                break
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = second
        return first
        
# Official solution

class Solution:
    def oddEvenList(self, head) :
        if not head:
            return None
        
        odd = head
        even = head.next
        evenHead = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = evenHead
        
        return head
