class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            x = token.strip("-")
            if x.isalnum():
                stack.append(int(token))
            else:
                x, y = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(int(x+y))
                if token == "-":
                    stack.append(int(y-x))
                if token == "/":
                    stack.append(int(y/x))
                if token == "*":
                    stack.append(int(x*y))
        return stack[-1]
                
    
                
                    

