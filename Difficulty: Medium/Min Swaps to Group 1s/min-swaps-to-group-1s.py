class Solution:
    def minSwaps(self, arr):
        count = 0 
        n = len(arr)
        ones = arr.count(1)
        if ones ==0:
            return -1
            
        left =0 
        swaps = n 
        for i in  range(n):
            count += arr[i]
            if i >= ones:
                count -= arr[left]
                left += 1
            if i>= ones-1:
                swaps = min(swaps,ones-count)
        return swaps
        # code here