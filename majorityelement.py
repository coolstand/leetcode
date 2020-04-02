class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        flag = None
        for x in nums:
            if n == 0:
                flag = x
            n += (1 if flag == x else -1)

        return flag 


if __name__ == '__main__':
    a = Solution()
    print(a.majorityElement([1,1,3]))
