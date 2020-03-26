import os
import sys

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    '''
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        first = head
        second = head.next

        first.next = self.swapPairs(second.next)
        second.next = first

        return second
    '''
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pHead = ListNode(0)
        pre, pre.next = pHead, head
        #pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a

        return pHead.next
        #return self.next


    def convList(self, s):
        if not s:
            return None
        head = ListNode(1)
        cur = head
        tmp = None
        for i in range(len(s), 0, -1):
            curVal = s[i-1:i]
            cur = ListNode(int(curVal))
            cur.next = tmp
            tmp = cur
            if i == 1:
                head = cur
        return head


if __name__ == '__main__':
    a = Solution()
    head = a.convList("1234")
    result = a.swapPairs(head)
    while result:
        print (result.val)
        result = result.next
