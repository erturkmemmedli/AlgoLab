# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head or not k:
            return head
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        k = k % length
        if k == 0:
            return head
        rot = length - k
        temp = head
        prev = None
        while rot:
            if rot == 1:
                prev = temp
            temp = temp.next
            rot -= 1
        newHead = temp
        if prev:
            prev.next = None
        tail = None
        while temp:
            if not temp.next:
                tail = temp
            temp = temp.next
        if tail:
            tail.next = head
        return newHead
        
# Official solution

class Solution:
    def rotateRight(self, head, rotations):

        if head is None or head.next is None or rotations <= 0:
            return head

        lastNode = head
        listLength = 1

        while lastNode.next is not None:
            lastNode = lastNode.next
            listLength += 1

        lastNode.next = head
        rotations %= listLength
        skipLength = listLength - rotations
        lastNodeOfRotatedList = head

        for i in range(skipLength - 1):
            lastNodeOfRotatedList = lastNodeOfRotatedList.next

        head = lastNodeOfRotatedList.next
        lastNodeOfRotatedList.next = None

        return head
