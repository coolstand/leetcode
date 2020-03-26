import os
import sys
import heapq


class KthLargest(object):
    """
    def __init__(self, k, nums):
        self.key = k
        self.nums = nums
        
    def add(self, val):
        print self.nums
        self.nums.append(val)
        self.nums.sort(reverse=True)
        print self.nums
        return self.nums[self.key-1]
    """
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.key = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.key:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]

        

if __name__ == '__main__':
    #a = KthLargest(3, [4,5,8,2])
    #print (a.add(5))

    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    for i in range (len(nums)-k+1):
        print (nums[i:i+k])