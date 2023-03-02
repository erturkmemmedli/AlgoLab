from heapq import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        heap = []
        dictionary = {i: lists[i] for i in range(len(lists))}

        for i, lst in enumerate(lists):
            if lst:
                heappush(heap, (lst.val, i))

        head = None
        temp = None

        while heap:
            val, idx = heappop(heap)

            if not head:
                head = dictionary[idx]
                temp = head
            else:
                temp.next = dictionary[idx]
                temp = temp.next

            if dictionary[idx].next:
                dictionary[idx] = dictionary[idx].next
                heappush(heap, (dictionary[idx].val, idx))

        return head
        
# Official solution

class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        current = dummy
        heap = []
        
        for index, list in enumerate(lists):
            if list:
                heap.append((list.val, index))
                
        heapify(heap)
        
        while heap:
            val, index = heappop(heap)
            current.next = ListNode(val)
            current = current.next
            node = lists[index].next

            if node:
                lists[index] = node

                heappush(heap, (node.val, index))
                
        return dummy.next
