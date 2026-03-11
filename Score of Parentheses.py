class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for par in s:
            if par =='(':
                stack.append(par)
            else:
                found = True
                a = 0
                while stack[-1] != '(':
                    a += stack.pop()
                    found = False
                if not found:
                    stack.pop()
                    stack.append(a * 2)
                else:
                    stack.pop()
                    stack.append(1)  
        return sum(stack)            

         
        
