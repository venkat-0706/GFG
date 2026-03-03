class Solution:
    def totalElements(self, arr):
        from collections import Counter
        cnt=Counter()
        mx=left=0
        for right,ve in enumerate(arr):
            cnt[ve]+=1
            while len(cnt)>2:
                cnt[arr[left]]-=1
                if cnt[arr[left]]==0:
                    cnt.pop(arr[left],None)
                left+=1
            mx=max(mx,right-left+1)
        return mx