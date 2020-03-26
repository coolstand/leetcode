import sys
import os

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        prev = None
        cur = head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

if __name__ == '__main__':
    '''
    node = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    node.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None

    a = Solution()
    result = a.reverseList(node)
    while result:
        print (result.val)
        result = result.next
    '''
    s = "13469"
    for i in range(len(s),0,-1):
        print ("pos:%d",i)
        print (s[i-1:i])
