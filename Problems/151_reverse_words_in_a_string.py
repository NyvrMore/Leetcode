"""
Given an input string, reverse the string word by word.

Example:  
Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = s.split()
        s = s[::-1]
        s = ' '.join(s)
        return s

"""
Explanation

We split the list based on white spaces, reverse the list, then join them back into a string seperated by a white space
"""