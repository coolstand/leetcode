import sys
import os

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

''' func1
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1head = self.reverseList(l1)
        l2head = self.reverseList(l2)

        tmpResult = self.formatNum(l1head) + self.formatNum(l2head)

        head = self.convList(str(tmpResult))
        resHead = self.reverseList(head)

        strResult = ""
        while resHead:
            strResult += str(resHead.val)
            resHead = resHead.next
        
        return self.convList(strResult)

    def reverseList(self, head):
        if not head:
            return head
        cur = head
        prev = None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
    
    def formatNum(self, head):
        if not head:
            return 0
        result = ""
        while head:
            result += str(head.val)
            head = head.next
        return int(result)
    
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
'''
    

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        cur = dummyHead
        carry = 0
        while l1 != None or l2 != None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            sum = x + y + carry
            carry = sum / 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if carry > 0:
            cur.next = ListNode(1)
        
        return dummyHead.next

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
    l1 = a.convList("243")
    l2 = a.convList("564")
    result = a.addTwoNumbers(l1,l2)
    print result
    while result:
        print (result.val)
        result = result.next