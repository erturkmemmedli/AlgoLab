# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        currPosition = 1
        tailFromLeft = None
        reverseHead = None
        temp = head
        while currPosition < left:
            tailFromLeft = temp
            currPosition += 1
            temp = temp.next
        reverseHead = temp
        prev, curr = None, reverseHead
        while currPosition <= right:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            currPosition += 1
        if tailFromLeft:
            tailFromLeft.next = prev
        else:
            head = prev
        reverseHead.next = curr
        return head
        
# Official solution

class Solution:
    def reverseBetween(self, head, left, right):

        if left == right:
            return head

        current = head
        prev = None
        i = 1

        while current != None and i < left:
            prev = current
            current = current.next
            i += 1

        lastNodeBeforeLeft = prev
        lastNodeOfSublist = current
        next = None

        while current != None and i <= right:
            next = current.next
            current.next = prev
            prev = current
            current = next
            i += 1

        if lastNodeBeforeLeft != None:
            lastNodeBeforeLeft.next = prev
        else:
            head = prev

        lastNodeOfSublist.next = current

        return head
