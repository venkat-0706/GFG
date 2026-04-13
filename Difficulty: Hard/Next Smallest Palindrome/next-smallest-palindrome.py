class Solution:
    def nextPalindrome(self, num):
        # code here
        n = len(num)
        if all(x == 9 for x in num):
            return [1] + [0] * (n - 1) + [1]
        mid = n // 2
        i = mid - 1
        j = mid + 1 if n % 2 else mid
        while i >= 0 and num[i] == num[j]:
            i -= 1
            j += 1
        leftsmaller = i < 0 or num[i] < num[j]
        while i >= 0:
            num[j] = num[i]
            i -= 1
            j += 1
        if leftsmaller:
            carry = 1
            if n % 2 == 1:
                num[mid] += carry
                carry = num[mid] // 10
                num[mid] %= 10
                j = mid + 1
            else:
                j = mid
            i = mid - 1
            while i >= 0 and carry:
                num[i] += carry
                carry = num[i] // 10
                num[i] %= 10
                num[j] = num[i]
                i -= 1
                j += 1
        return num