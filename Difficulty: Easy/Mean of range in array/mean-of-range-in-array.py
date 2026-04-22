class Solution:
    def findMean(self, arr, queries):
        n = len(arr)
        # Build prefix sum array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]
        
        result = []
        for l, r in queries:
            # Length of subarray [l, r]
            length = r - l + 1
            # Sum of subarray [l, r]
            total = prefix[r + 1] - prefix[l]
            # Mean floored
            mean_floor = total // length
            result.append(mean_floor)
        return result