import sys
import os

class Solution(object):
    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,vi in enumerate(nums):
            for j,vj in enumerate(nums):
                if vi + vj == target and i != j:
                    return [i,j]
        return []

    def twoSum_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i,vi in enumerate(nums):
            m[vi] = i
        for k,vk in enumerate(nums):
            if m.get(target-vk) and m[target-vk] != k:
                return [k, m[target-vk]]
        return []

    def twoSum_3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in m:
                return [m[tmp], i]
            m[nums[i]]=i
        return []
 
if __name__ == '__main__':
    a = Solution()
    print (a.twoSum_1([2,7,11,15], 9))
    #print (a.twoSum_2([0,4,3,0], 0))
    #print (a.twoSum_3([3,3], 6))

