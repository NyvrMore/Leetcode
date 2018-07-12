"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
                
        for c in t:
            if c not in d:
                return False
            else:
                d[c] -= 1
                
        for key in d.keys():
            if d[key] != 0:
                return False
        return True

"""
Explanation

An anagram is just a different order of the same characters. Therefore, we just add each character to a dictionary and track its frequency.

We then look through the second string and if the character is not in the dictionary, we return false since they dont
contain the same words. If they do, we subtract its frequency count. Lastly, we loop through all keys and if it's frequency is not equal to 0, then 
they dont match, otherwise it's an anagram
"""