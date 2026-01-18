class Solution:
    def nextFreqGreater(self, arr):
        from collections import Counter
        count = Counter(arr)
        res = [-1]*len(arr)
        ans = []
        for ind , ele in enumerate(arr):
            while ans and count[arr[ans[-1]]] < count[ele]:
                res[ans.pop()]=ele
            ans.append(ind)
        return res