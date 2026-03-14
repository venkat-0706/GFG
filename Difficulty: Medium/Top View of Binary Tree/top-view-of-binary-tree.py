from collections import defaultdict, deque

class Solution:
    def topView(self, root):
        hashmap = defaultdict(int)
        
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            
            if level not in hashmap:
                hashmap[level] = node.data
                
            if node.left:
                queue.append((node.left, level-1))

            if node.right:
                queue.append((node.right, level+1))
        
        res = [val for _, val in sorted(hashmap.items())]
        return res