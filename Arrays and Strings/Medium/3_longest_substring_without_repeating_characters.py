"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        d = {}
        ptr = 0
        length = 0
        for index, c in enumerate(s):
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
                
            while d[c] > 1:
                d[s[ptr]] -= 1
                ptr += 1
            length = max(length, index - ptr + 1)
        return length

"""
Explanation

We use a dictionary to track all the elements in the current substring we're considering. We use a ptr to consider the last non-repeating character.
We then loop through each character and increase it's frequency. After we update a character's frequency, if that character already exists in the row (i.e. freq > 1)
then we subtract the frequency of each character and move right until the character's frequency becomes 1 again. After each loop, we update length to be the difference between our 
current index and the ptr against the current length.


"""