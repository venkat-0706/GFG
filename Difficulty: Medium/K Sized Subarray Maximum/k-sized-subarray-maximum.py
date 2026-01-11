class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        q, ans = [] ,[]
        for i , e in enumerate(arr):
            while q and arr[q[-1]] <= e:
                q.pop()
            q.append(i)
            while q and q[0]+k <= i:
                q.pop(0)
            if  i>= k-1:
                ans.append(arr[q[0]])
        return ans
        