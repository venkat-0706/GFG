class Solution:
    def stableMarriage(self, men, women):
        n = len(men)
        
        rank = [[0]*n for _ in range(n)]
        for w in range(n):
            for i in range(n):
                rank[w][women[w][i]] = i
                
        free_men = list(range(n))
        next_proposal = [0]*n
        woman_partner = [-1]*n
        man_partner = [-1]*n
        
        while free_men:
            m = free_men.pop(0)
            w = men[m][next_proposal[m]]
            next_proposal[m] += 1
            
            if woman_partner[w] == -1:
                woman_partner[w] = m
                man_partner[m] = w
            else:
                current = woman_partner[w]
                
                if rank[w][m] < rank[w][current]:
                    woman_partner[w] = m
                    man_partner[m] = w
                    man_partner[current] = -1
                    free_men.append(current)
                    
                else:
                    free_men.append(m)
                    
        return man_partner
        