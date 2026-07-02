class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = { "}" : "{" , ")" : "(" , "]" : "["}

        for n in s:
            if n in close_to_open:
                if stack and stack[-1] == close_to_open[n]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(n)
        return True if not stack else False