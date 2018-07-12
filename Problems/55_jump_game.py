"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false

Explanation: 
You will always arrive at index 3 no matter what. Its maximum
jump length is 0, which makes it impossible to reach the last index.
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        
        if n == 0:
            return False
        
        if n == 1:
            return True
        
        d = {}
        d[0] = nums[0]
        
        for i in range(1, len(nums)):
            d[i] = max(d[i-1]-1, nums[i])
            if d[i] <= 0 and i < len(nums) - 1:
                return False
        return True

"""
Explanation

Base Cases:
1. If nums is empty, we return False
2. If nums is of length 1, we're at the final index

We use a dictionary to store the results for each index. We are originally posirive at the first index
so the number of jumps we initially start with is nums[0]

At each state, the number of jumps we have available is the maximum of either the number of jumps we can do from our current index of one less the number of jumps we had at the previous state. Therefore,

OPT(i) = max(OPT(i-1) - 1, OPT(i))

At each state, after we determined the the number of jumps, if the number of jummps <= 0 and we're not at the final index, then we return False. Otherwise, we return True

We can also use an array of length n to store the results. 

"""