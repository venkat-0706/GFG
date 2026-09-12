class Solution:
    def maxProduct(self, arr: list[int], k: int) -> int:
        arr.sort()
        n = len(arr)
        prod = 1

        if arr[-1] <= 0 and (k % 2 == 1):
            for i in range(n - 1, n - 1 - k, -1):
                prod *= arr[i]
            return prod

        left = 0
        right = n - 1

        if k % 2 == 1:
            prod *= arr[right]
            right -= 1
            k -= 1

        while k > 0:
            left_prod = arr[left] * arr[left + 1]
            right_prod = arr[right] * arr[right - 1]

            if left_prod > right_prod:
                prod *= left_prod
                left += 2
            else:
                prod *= right_prod
                right -= 2
            k -= 2

        return prod