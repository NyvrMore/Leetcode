"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums == []:
            return 0
        
        if len(nums) == 1:
            return 1
        
        prev = nums[0]
        length = 1
        pointer = 1
        for i in range(1, len(nums)):
            if nums[i] != prev:
                nums[pointer] = nums[i]
                prev = nums[i]
                pointer += 1
                length += 1
        return length

"""
Explanation

Since we are not allowed to allocate space, we will simply use a pointer to indicate the location that we need to swap "non-duplicates" to.
The base cases are when the input is empty or length 1 (which means no duplicates). Now we can handle all cases where n >= 2. The first element will
will never be duplicate, so we put our pointer at index 1. We also track the previous number considered so initally it's the number at index 0. We
then loop through the list and as long as our current number isn't equal to the previous, we swap our current number with the number at the pointer index.
We then increment pointer and the length.
"""