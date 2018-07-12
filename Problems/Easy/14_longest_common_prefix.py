"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ""
        if len(strs) == 0:
            return output

        minLength = len(strs[0])
        for i in range(1, len(strs)):
            minLength = min(minLength, len(strs[i]))

        isPrefix = True
        for i in range(minLength):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if c != strs[j][i]:
                    isPrefix = False

            if isPrefix:
                output += c
            else:
                return output
        return output

"""
Explanation

If the input is empty, return "". The longest the prefix will be is the length of the minimum string.
c represents each character in the first string. For each character in the first string, we loop through the 
corresponding index of all the rest of the strings. If the rest of the strings have that character, we add it
to the output string, otherwise we return the output

e.g. In the first look, c is 'f', then we loop throught the rest of the strings if the index at 0 is 'f' 
"""