class Solution(object):
    '''
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for x in nums:
            if not dic.has_key(x):
                dic[x] = 1
            else:
                dic[x] += 1
        for x in dic:
            if dic[x] == 1:
                return x
        return 0
    '''
    def singleNumber(self, nums):
        a = 0
        for x in nums:
            a ^= x
        
        return a



if __name__ == '__main__':
    a = Solution()
    print(a.singleNumber([1,1,3]))
    #a = 3
    #print (a ^ a)
    
