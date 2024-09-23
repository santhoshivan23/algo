class Solution:
    def isValid(self, s: str) -> bool:
        openings = ["(", "{", "["]
        closings = [")", "}", "]"]
        mappings = { 
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []
        for ch in s:
            if ch in openings:
                stack.append(ch)
            else:
                if len(stack) != 0 and stack[-1] == mappings[ch]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        
        
# https://leetcode.com/problems/valid-parentheses/