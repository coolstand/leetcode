'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lResult = [[]]

        for num in nums:
            lResult += [cur + [num] for cur in lResult]
        
        print (lResult)

    
class Solution:
    def subsets(self, nums):
        def backtrack(first, curr):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
    
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack(k, nums)
        return output
'''

class Solution:
    def subsets(self, nums):
        n = len(nums)
        bitmask = 1 << n
        output = []

        for i in range(2**n):
            bitmask = bin(i | 1 << n)[3:]
            #print (bitmask)
            a = (nums[j] for j in range(n) if bitmask[j] == '1')
            ltemp = []
            for x in a:
                ltemp.append(x)
            #print (ltemp)
            output.append(ltemp)
        
        return output

if __name__ == '__main__':
    a = Solution()
    a.subsets([1,2,3])
    #n = 3
    #print (2**n)
    #print (1 << n)
    #for i in range(2**n):
    #    print (i, 1<<n, bitmask)
