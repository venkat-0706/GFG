        
class kQueues:

    def __init__(self, n, k):
        # Initialize your data members

        self.store = [0]*n
        self.qs = [[] for _ in range(k)]
        self.count = 0
        self.size = n
        self.slots = list(range(n))
    

    def enqueue(self, x, i):
        # Enqueue element x into queue number i
        if self.isFull():
            return False
        idx = self.slots.pop()
        self.qs[i].append(idx)
        self.store[idx] = x
        self.count += 1

    def dequeue(self, i):
        # Dequeue element from queue number i
        if self.isEmpty(i):
            return -1
        idx = self.qs[i].pop(0)
        self.slots.append(idx)
        self.count -= 1
        return self.store[idx] 

    def isEmpty(self, i):
        # Check if queue i is empty
        return len(self.qs[i]) == 0
        
    def isFull(self):
        # Check if array is full
        return self.count == self.size