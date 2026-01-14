class Solution:
    def catchThieves(self, arr, k):
        #code here
        n = len(arr)
        police , thief = 0,0
        while  police < n and arr[police]!= 'P':
            police += 1
        while thief <n and arr[thief]!= 'T':
            thief += 1
        count = 0
        while police <n and thief < n:
            if abs(police - thief) <=k:
                police += 1
                thief += 1
                count += 1
            elif police <n and police < thief :
                police += 1
            elif thief <n and thief  < police :
                thief += 1
            while police < n and  arr[police]!='P':
                police += 1
            while thief < n and arr[thief] != 'T':
                thief += 1
        return count
        

