class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)
        curr_sum =0 
        for i in range(0,k):
            curr_sum ^= arr[i]
        max_sum = curr_sum 
        for i in range(k,n):
            curr_sum ^= arr[i-k]
            curr_sum ^= arr[i]
            max_sum = max(max_sum , curr_sum)
        return max_sum
       

       