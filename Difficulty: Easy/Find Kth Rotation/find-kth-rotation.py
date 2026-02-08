class Solution:
    def findKRotation(self, arr):
        low, high = 0, len(arr) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] <= arr[-1]:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
        