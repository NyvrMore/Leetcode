"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        output = ""
        for c in s:
        	output += c
        return output

        wordlist = s.split()
        for i in range(len(wordlist)):
            wordlist[i] = wordlist[i][::-1]
        
        return ' '.join(wordlist)

"""
Explanation

We split the words using white space as a delimter, and reverse the words seperately
"""