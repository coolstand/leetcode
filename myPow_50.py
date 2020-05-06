class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return float(1)
        if n == 1:
            return float(x)
        i = 1
        res = 1
        new = abs(n)
        if n & 1 == 0:
            res = self.myPow(x, new/2)
            result = res * res
            if n > 0:
                return result
            return 1 / result
        elif n & 1 == 1:
            res = self.myPow(x, (new-1)/2)
            result = res * res * x
            if n > 0:
                return result
            return 1 / result

if __name__ == '__main__':
    a = Solution()
    print (a.myPow(5.6,1))
