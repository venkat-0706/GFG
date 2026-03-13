class Solution:
    def generateIp(self, s):
        res = []
        def backtrack(start, parts, path):
            if parts == 4:
                if start == len(s):
                    res.append(".".join(path))
                return 
            
            for l in range(1,4):
                if start + l > len(s):
                    break 
                part = s[start:start+l]
                
                if len(part) > 1 and part[0] == '0':
                    continue
                
                if int(part) <= 255:
                    backtrack(start + l, parts + 1, path + [part])
                    
        backtrack(0, 0, [])
        return res