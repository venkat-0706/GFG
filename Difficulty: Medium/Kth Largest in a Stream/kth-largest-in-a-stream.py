class Solution:
    def kthLargest(self, arr, n):
        ret=[]
        import heapq
        hp=[]
        for ve in arr:
            heapq.heappush(hp,ve)
            if len(hp)>n:
                heapq.heappop(hp)
            ret.append(-1)
            if len(hp)==n:
                ret[-1]=hp[0]
        return ret