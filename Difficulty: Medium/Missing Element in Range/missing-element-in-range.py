class Solution:
    def missingRange(self, arr, low, high):
        nums = set(arr)
        res = []
        for num in range(low,high+1):
            if num not in nums:
                res.append(num)
        return res