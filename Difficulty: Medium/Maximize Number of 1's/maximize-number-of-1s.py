class Solution:
    def maxOnes(self, arr, k):
        c=0
        n=len(arr)
        i,j=-1,0
        ans=0
        while j<n:
            if arr[j]==0:
                if c<k:
                    c += 1
                else:
                    i += 1
                    while arr[i]:
                        i += 1
            ans=max(ans,j-i)
            j += 1
        return ans
            