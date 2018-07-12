"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf()
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needleLength = len(needle)
        haystackLength = len(haystack)
        if haystackLength < needleLength:
            return -1

        for i in range(haystackLength - needleLength + 1):
            if haystack[i:needleLength + i] == needle:
                return i
        return -1

"""
Explanation

We get the length of the needle and haystack. Then we just loop through the haystack and search for the needle if it exists
"""