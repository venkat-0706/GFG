class Solution:
    def maxOnes(self, arr):
        mx=cur=cnt=0
        for ve in arr:
            cnt+=1 if ve==1 else 0
            cur+=1 if ve==0 else -1
            cur=max(cur,0)
            mx=max(mx,cur)
        return cnt+mx