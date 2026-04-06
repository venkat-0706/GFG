import heapq

class Node:
    def __init__(self, val=None, sum_=0, idx=-1):
        self.val = val
        self.sum = sum_
        self.idx = idx
        self.left = None
        self.right = None

    # needed for heap comparison
    def __lt__(self, other):
        if self.sum != other.sum:
            return self.sum < other.sum
        return self.idx < other.idx

def preorder(root, path, mp):
    if not root:
        return
    
    if root.val is not None:
        mp[root.val] = path if path != "" else "0"
    
    preorder(root.left, path + '0', mp)
    preorder(root.right, path + '1', mp)


class Solution:
    def huffmanCodes(self, s, f):
        # code here
        pq = []
        
        for i in range(len(s)):
            heapq.heappush(pq, Node(s[i], f[i], i))
        
        while len(pq) > 1:
            t1 = heapq.heappop(pq)
            t2 = heapq.heappop(pq)
            
            temp = Node(None, t1.sum + t2.sum, min(t1.idx, t2.idx))
            temp.left = t1
            temp.right = t2
            
            heapq.heappush(pq, temp)
        
        mp = {}
        preorder(pq[0], "", mp)
        
        return sorted([mp[ch] for ch in s])