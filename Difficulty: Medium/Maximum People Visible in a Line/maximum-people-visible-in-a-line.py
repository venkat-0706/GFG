class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        
        left = [-1] * n
        right = [n] * n
        stack = []

        # Nearest greater or equal element on the left
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        # Nearest greater or equal element on the right
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        maxCount = 0
        for i in range(n):
            maxCount = max(maxCount, right[i] - left[i] - 1)

        return maxCount

