"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n)
"""
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        if nums is None or len(nums) == 0:
            return 0
        
        i = j = mySum = 0
        minLength = len(nums) + 1
        
        while j < len(nums):
            mySum += nums[j]
            j += 1
            
            while mySum >= s:
                minLength = min(minLength, j - i)
                mySum -= nums[i]
                i += 1
                
        if minLength == len(nums) + 1:
            return 0
        else:
            return minLength

"""
Explanation

Base Cases:
1. Nums is None -> return 0
2. Nums is empty -> return 0

Have 2 pointers and sum initialized to 0. 

j is our right index that we move as far right as possible while our sum >= s. AFter each element, if our sum is >= s, we move the left index right sa much as possible until sum < s:
Each time we move the ith index left, we first take the minimum  between i and j and our current minimum distance (initially set to the length of the list + 1). 

After exmaining all elements, if the minLength hasn't changed, we return -1, otherwise we return the minLength
"""