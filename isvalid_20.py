# -*- coding: utf-8 -*-
import os
import sys

print (sys.getdefaultencoding())
reload(sys)
sys.setdefaultencoding('utf8')

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        queue = []
        parent = {')':'(', ']':'[', '}':'{'}
        for x in s:
            if x not in parent:
                #当前进入的是左括号，则加入队列
                queue.append(x)
            else:
                #当前进入的是右括号
                if not queue:
                    #说明之前没有左括号
                    return False
                else:
                    #队列里有东西
                    #从队列的最后面pop一个字符，看是否和当前的右括号匹配
                    if parent[x] != queue.pop():
                        return False
        #队列中如果还有字符，说明没有匹配完，则为false
        return not queue

if __name__ == '__main__':
    a = Solution()
    print (a.isValid("{()}"))