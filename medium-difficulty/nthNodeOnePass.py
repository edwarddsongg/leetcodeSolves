class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node_arr = []
        temp = head
        while (temp):
            node_arr.append(temp)
            temp = temp.next
        if (len(node_arr ) == 1): 
            return None
        if (len(node_arr) - n <= 0): return node_arr[1]
        node = node_arr[len(node_arr)-1-n]
        node.next= node.next.next
        return head


print(ord("b")-97)