"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be 
a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		if len(s) < 2:
			return len(s)
        
		maxLength = 0
		seen = {}
		i = j = 0
		while i < len(s):
			if s[i] not in seen:
				seen[s[i]] = 1
			else:
				maxLength = max(maxLength, len(seen.keys()))
				while s[i] in seen and j < i:
					if s[i] != s[j]:
						del seen[s[j]]
						j += 1
					else:
						j += 1
			i += 1
		maxLength = max(maxLength, len(seen.keys()))
		return maxLength

"""
Explanation:

For the base cases, we handle when n is less than 2:
 - The longest a substring of an empty string is 0
 - The longest a substring of a string with one character is 1

We maintain a dictionary that keeps track of all the strings we are currently tracking and two pointers, left and right
 - left: tracks the left most non-repeating element
 - right tracks the current element we are considering

Loop:
For each character that's not in the dictionary, we add it to the dictionary. Otherwise, if it's in the dictionary then we update the 
maxlength and move the left pointer, removing the element it's pointing to from the ctionary, until it's not in the dictionary and it's different than the 
previous value (that is, any duplicates of the same letter are skipped. 

Since we update the maxLength only when we see a duplicate in the list, we must update the maxLength after the foor loop as well (this handles the case where no repeating decimals are found)
"""

