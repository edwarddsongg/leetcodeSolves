# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        track = start = head 

        i = 0

        while track is not None:
            i+=1 
            track = track.next

        if i == 1: 
            return None 

        index = i-n

        if index == 0:
            return start.next

        i = 0
        track = start
        while True:
            if i == index - 1:
                if track.next.next is None:
                    track.next = None
                else:
                    print(track.val)
                    track.next = track.next.next
                break
            else:
                track = track.next
                i+=1

        return start
        
        
