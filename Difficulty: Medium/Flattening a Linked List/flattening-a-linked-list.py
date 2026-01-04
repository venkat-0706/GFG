'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def flatten(self, root):
        curr = root
        vals=[]
        while curr:
            vals.append(curr.data)
            if curr.bottom:
                bom=curr.bottom
                while bom:
                    vals.append(bom.data)
                    bom=bom.bottom
            curr = curr.next
        vals.sort()
        ans=head=Node(vals[0])
        for i in vals[1:]:
            head.bottom=Node(i)
            head=head.bottom
        return ans