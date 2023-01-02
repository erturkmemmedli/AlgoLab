# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy
        temp1 = list1
        temp2 = list2
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                current.next = temp1
                temp1 = temp1.next
            else:
                current.next = temp2
                temp2 = temp2.next
            current = current.next
        current.next = temp1 if temp1 else temp2
        return dummy.next
		
# Official solution given

class Solution:
    def mergeTwoLists(self, list1, list2):
        newHead = ListNode(0)
        newList = newHead

        while list1 and list2:

            if list1.val < list2.val:
                newList.next = ListNode(list1.val)
                list1 = list1.next
            else:
                newList.next = ListNode(list2.val)
                list2 = list2.next

            newList = newList.next

        while list1:
            newList.next = ListNode(list1.val)
            list1 = list1.next
            newList = newList.next

        while list2:
            newList.next = ListNode(list2.val)
            list2 = list2.next
            newList = newList.next

        return newHead.next