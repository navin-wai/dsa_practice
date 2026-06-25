class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #ok so we can make a stack , so we insert the element in the stack if its a number
        #but if its a operator , we pop the top 2 elements and perform that operation on them 
        #and store their result on the top and after this is done , the last element after 
        #going around the whole array should be the output that we need

        stack = []

        for n in tokens:
            if n == "+":
                stack.append(stack.pop()+ stack.pop())  
            elif n == "*":
                stack.append(stack.pop() * stack.pop())
            elif n == "-":
                a = stack.pop() 
                stack.append(stack.pop() - a)
            elif n == "/":
                a = stack.pop()
                stack.append(int(stack.pop() / a))
            else:
                stack.append(int(n))
        return stack[0]