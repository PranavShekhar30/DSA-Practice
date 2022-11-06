class Solution(object):
    def twoSum(self, nums, target):
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff not in dict:
                dict[n] = i
            else:
                return [dict[diff], i]
        