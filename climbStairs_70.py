class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        if n == 1:
            return 1
        
        prepre, prev = 1,1
        for i in range(2, n+1):
            res = prepre + prev
            prepre, prev = prev, res
        
        return res

if __name__ == '__main__':
    a = Solution()
    print (a.climbStairs(5))
