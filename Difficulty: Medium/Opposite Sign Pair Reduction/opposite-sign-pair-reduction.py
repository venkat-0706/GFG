class Solution:
    def reducePairs(self, arr):
        stack = []
        
        for x in arr:
            while stack and ((stack[-1] > 0 and x < 0) or (stack[-1] < 0 and x > 0)):
                
                if abs(stack[-1]) > abs(x):
                    break
                
                elif abs(stack[-1]) < abs(x):
                    stack.pop()
                
                else:
                    stack.pop()
                    break
            else:
                stack.append(x)
        
        return stack