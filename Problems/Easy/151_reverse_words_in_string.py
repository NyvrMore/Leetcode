"""
Given an input string, reverse the string word by word.

Example:  

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        wordlist = s.split()
        wordlist = wordlist[::-1]
        output = ""
        for word in wordlist:
            output += word + " "
        return output[:len(output) - 1]

"""
Explanation

Split the list on white spaces. Reverse the list. Then loop through the list
and append it our result to get the output string.
"""