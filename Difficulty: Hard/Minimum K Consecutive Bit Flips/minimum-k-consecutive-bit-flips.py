class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        isflipped = [0] * n
        flip = 0
        ans = 0
        
        for i in range(n):
            if i >= k:
                flip ^= isflipped[i - k]
            if arr[i] ^ flip == 0:
                if i + k > n:
                    return -1
                ans += 1
                flip ^= 1
                isflipped[i] = 1
        return ans