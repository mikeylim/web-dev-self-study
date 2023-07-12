# 20. Valid Parentheses
# Easy
# 20.7K
# 1.3K
# Companies
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for str in s:
            if str == "(" or str == "[" or str == "{":
                stack.append(str)
            elif str == ")" and "(" in stack:
                stack.pop()
            elif str == "]" and "[" in stack:
                stack.pop()
            elif str == "}" and "{" in stack:
                stack.pop()
            else:
                return False
        return not stack
            
sol = Solution()
# print(sol.isValid("()"))
# print(sol.isValid("()[]{}"))
# print(sol.isValid("(]"))
# print(sol.isValid("{}[]"))
# print(sol.isValid("({})"))
# print(sol.isValid("({}))"))
# print(sol.isValid("({{{{}}}))")) # weird case
