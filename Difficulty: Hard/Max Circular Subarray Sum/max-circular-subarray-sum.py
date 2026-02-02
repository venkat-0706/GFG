class Solution:
    def maxCircularSum(self, arr):
        n = len(arr)
        curr_max = max_sum  = curr_min = min_sum  = arr[0]
        total_sum = arr[0]
        for i in range(1,n):
            curr_max = max(arr[i], arr[i]+curr_max)
            max_sum  =max(max_sum ,curr_max)
            curr_min =  min(arr[i], arr[i]+curr_min)
            min_sum = min(curr_min , min_sum)
            
            total_sum += arr[i]
            
        if min_sum == total_sum :
            return max_sum 
        return max(max_sum , total_sum - min_sum)
        