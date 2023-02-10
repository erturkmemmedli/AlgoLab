# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        # Mathematical proof

        # o -> o -> o -> o -> o -> o -> o -> o -> o
        #           ^                             |
        #           |_____________________________|
        #
        # <___ x ___><___ k ___><_____ y - k _____>
        #
        # assume length of linked list = x + y
        # cycle starts at position x
        # hare and tortoise meet at position x + k
        #
        # length of path of tortoise = x + k
        # length of path of hare = x + y + k
        #
        # we know that hare is 2x faster than tortoise
        # 2 * x + 2 * k = x + y + k   =>   x = y - k
        #
        # So, now if we move with the same speed,
        # distance from 0 to x (which is x) = distance from x + k to k (which is y - k)

        hare = tortoise = head
        cycyleStartPoint, hareAndTortoiseMeetingPoint = head, None
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                hareAndTortoiseMeetingPoint = hare
                break
        if not hareAndTortoiseMeetingPoint: return
        while cycyleStartPoint != hareAndTortoiseMeetingPoint:
            cycyleStartPoint = cycyleStartPoint.next
            hareAndTortoiseMeetingPoint = hareAndTortoiseMeetingPoint.next
        return cycyleStartPoint
        
# Official solution

class Solution:
    def detectCycle(self, head):
        if head is None:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                p1 = head
                p2 = slow

                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next

                return p1

        return None
