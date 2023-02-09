# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        count = length // k
        if count == 0:
            return head
        prev = None
        curr = head
        tail = head
        x = k
        while x:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            x -= 1
        tail.next = self.reverseKGroup(curr, k)
        return prev

# Official solution

class Solution:
    def reverseKGroup(self, head, k):
        temp = head
        length = 0

        while temp != None:
            length += 1
            temp = temp.next

        current = head
        prev = None

        while current != None:
            nodeBeforeSublist = prev
            lastNodeOfSublist = current
            next = None
            i = 0

            while current != None and i < k:
                next = current.next
                current.next = prev
                prev = current
                current = next
                i += 1

            if nodeBeforeSublist != None:
                nodeBeforeSublist.next = prev
            else:
                head = prev

            lastNodeOfSublist.next = current

            length -= k

            if current == None or length < k:
                break

            prev = lastNodeOfSublist

        return head
