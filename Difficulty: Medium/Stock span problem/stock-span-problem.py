class Solution:
    def calculateSpan(self, arr):
        stack = []
        ans = []
        for i , e in enumerate(arr):
            while stack and arr[stack[-1]] <= e:
                stack.pop()
            if stack:
                ans.append(i-stack[-1])
            else:
                ans.append(i+1)
            stack.append(i)
        return ans
        
        