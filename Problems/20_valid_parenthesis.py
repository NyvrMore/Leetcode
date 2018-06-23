"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

class Solution(object):
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        pairs = {'{':'}','[':']','(':')'}
        
        if len(s) % 2 == 1:
            return False
        
        for c in s:
            if c in pairs.keys():
                stack.append(c)
            elif c in pairs.values() and len(stack)  == 0:
                return False
            elif c in pairs.values():
                if c == pairs[stack[-1]]:
                    stack.pop()
                    
        if len(stack) == 0:
            return True
        else:
            return False