class Solution(object):
    def twoSum(self, nums, target):
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complementMap = dict()
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if nums[i] in complementMap:
                return [complementMap[nums[i]], i]
            else:
                complementMap[complement] = i
        