class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if len(nums) == 0:
            return -1
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        return -1