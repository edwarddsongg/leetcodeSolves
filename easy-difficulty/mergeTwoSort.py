# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = None
        l1 = list1
        l2 = list2
        head = None
        if l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    temp = head = ListNode(l1.val)
                    l1 = l1.next
                else:
                    temp = head = ListNode(l2.val)
                    l2 = l2.next
            else:
                if l1: return l1
                if l2: return l2

        while l2 and l1:
            if l1.val <= l2.val:
                temp.next = l1
                print(temp.val, "?")
                l1 = l1.next
                temp = temp.next
            else:
                temp.next = l2
                print(temp.val, "?d")
                l2 = l2.next
                temp = temp.next

        if l2:
            temp.next = l2
        if l1:
            temp.next = l1

        return head
             