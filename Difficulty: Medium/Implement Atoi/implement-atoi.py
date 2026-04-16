class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()                     
        if not s: return 0
        sign, res, i = 1, 0, 0

        if s[i] in '+-':                   
            sign = -1 if s[i] == '-' else 1
            i += 1

        while i < len(s) and s[i].isdigit():  
            d = int(s[i])
            if res > (2**31 - 1)//10 or (res == (2**31 - 1)//10 and d > 7):
                return (2**31 - 1) if sign == 1 else -2**31
            res = res * 10 + d
            i += 1

        return sign * res