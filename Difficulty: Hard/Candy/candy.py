class Solution:
    def minCandy(self, arr):
        n = len(arr)
        candy = [1]*n
        for i in range(1,n):
            if arr[i] > arr[i-1]:
                candy[i] = candy[i-1]+1
        for i in range(n-2,-1,-1):
            if arr[i]> arr[i+1]:
                candy[i] = max(candy[i],candy[i+1]+1)
        return sum(candy)