import math

class Solution:
    def kokoEat(self, arr, k):
        l=1
        h=max(arr)
        while l<=h:
            sum=0
            rate=l+(h-l)//2
            for j in arr:
                if j%rate==0:
                    sum+=(j//rate)
                else:
                    sum+=((j//rate)+1)
            if sum<=k:
                ans=rate
                h=rate-1
            else:
                l=rate+1
            
        return ans