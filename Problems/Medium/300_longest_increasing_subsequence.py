"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        if n == 0:
            return n

        maxLen = 1
        DP = [1 for i in range(n)]
        

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    DP[i] = max(DP[j] + 1, DP[i])
                    maxLen = max(DP[i], maxLen)
        return maxLen

"""
Explanation

if nums is empty, then the longest increase subsequence is 0, otherwise it's 1 initially (i.e. 1 character)

We use an array of length n filled with 1's since the longest increasing subsequence of a single character is 1.

This question is essnetially asking what's the largest sequence of numbers such that they're sorted.

For each element, we loop through all prior elements and check them against the current element we're on.
If the prior element is less than the current, the longest increasing subsequence is the max between the longest increasing
subsequence at that point at j + 1 or the current index.

We use a variable to track the maxLen which updates whenever we update DP[i] and we return maxLen at the end



"""