class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s[0] == "]" or s[0] ==  ")"  or s[0] == "}":
            return False
        for n in s:
            if n == "}":
                if len(stack) == 0: return False
                if stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(n)
            elif n == "]":
                if len(stack) == 0 : return False
                if stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(n)
            elif n == ")":
                if len(stack) == 0 : return False
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(n)
            else : 
                stack.append(n)
        if len(stack) == 0:
            return True
        else:
            return False
