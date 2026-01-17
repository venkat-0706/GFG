class Solution():
    def checkRedundancy(self, s):
        # code here 
        res = []
        for i in s:
            res.append(i)
            if res[-1] == ")":
                if res[-2] == "(" or res[-3] == "(":
                    return True
                else:
                    while res[-1] !="(":
                        res.pop()
                    res.pop()
        return False
            