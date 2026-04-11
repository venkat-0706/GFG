class Solution:
    def countIncreasing(self, arr):
        curr_count =  0 
        total = 0 
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                curr_count += 1 
                total += curr_count 
            else:
                curr_count = 0 
        return total