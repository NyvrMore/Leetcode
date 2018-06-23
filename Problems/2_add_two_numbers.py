"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return 
        
        curr = l1
        l1Sum = 0
        index = 0
        while curr is not None:
            l1Sum += curr.val * 10 ** index
            curr = curr.next
            index += 1
        
        curr = l2
        l2Sum = 0
        index = 0
        while curr is not None:
            l2Sum += curr.val * 10 ** index
            curr = curr.next
            index += 1
            
        l3Sum = l1Sum + l2Sum
        rem = l3Sum % 10
        l3Sum = l3Sum / 10
        l3Node = ListNode(rem)
        curr = l3Node
        while l3Sum != 0:
            rem = l3Sum % 10
            l3Sum /= 10
            curr.next = ListNode(rem)
            curr = curr.next
        return l3Node