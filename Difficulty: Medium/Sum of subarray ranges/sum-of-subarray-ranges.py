class Solution:
    def subarrayRanges(self, arr):
        n = len(arr)

        def sumSubarrayMins():
            stack = []
            prev_less = [-1] * n
            next_less = [n] * n

            # Previous Less
            for i in range(n):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                prev_less[i] = stack[-1] if stack else -1
                stack.append(i)

            stack.clear()

            # Next Less or Equal
            for i in range(n - 1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                next_less[i] = stack[-1] if stack else n
                stack.append(i)

            total = 0
            for i in range(n):
                total += arr[i] * (i - prev_less[i]) * (next_less[i] - i)
            return total

        def sumSubarrayMaxs():
            stack = []
            prev_greater = [-1] * n
            next_greater = [n] * n

            # Previous Greater
            for i in range(n):
                while stack and arr[stack[-1]] < arr[i]:
                    stack.pop()
                prev_greater[i] = stack[-1] if stack else -1
                stack.append(i)

            stack.clear()

            # Next Greater or Equal
            for i in range(n - 1, -1, -1):
                while stack and arr[stack[-1]] <= arr[i]:
                    stack.pop()
                next_greater[i] = stack[-1] if stack else n
                stack.append(i)

            total = 0
            for i in range(n):
                total += arr[i] * (i - prev_greater[i]) * (next_greater[i] - i)
            return total

        return sumSubarrayMaxs() - sumSubarrayMins()