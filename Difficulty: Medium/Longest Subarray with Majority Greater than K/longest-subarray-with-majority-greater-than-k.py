class Solution:

    def longestSubarray(self, arr, k):

        n = len(arr)

        # Step 1: Transform array

        b = [1 if x > k else -1 for x in arr]

        

        # Step 2: Compute prefix sum

        prefix = [0] * (n + 1)

        for i in range(n):

            prefix[i+1] = prefix[i] + b[i]

        

        # Step 3: Build a decreasing stack of prefix indices

        stack = []

        for i in range(n+1):

            if not stack or prefix[i] < prefix[stack[-1]]:

                stack.append(i)

        

        # Step 4: Traverse from the end to find max length

        max_len = 0

        for j in range(n, -1, -1):

            while stack and prefix[j] > prefix[stack[-1]]:

                max_len = max(max_len, j - stack[-1])

                stack.pop()

        

        return max_len