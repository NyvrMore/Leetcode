"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

class Solution(object):   
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        d = {}
        for str in strs:
            key = "".join(sorted(str))
            if key in d:
                d[key].append(str)
            else:
                d[key] = [str]
        
        res = []
        for values in d.values():
            res.append(values)
        return res

"""
Explanation

For each anagram, we sort the string and check if the sorted version exists in the dictionary, if it does we append it to the list of similar anagrams, otherwise we append a new list that holds that value

We then create a results list and for each key, we append the list of anagrams paired with it

"""