class Solution:
	def pythagoreanTriplet(self, given):
	    A = sorted(list(set(given)), reverse = True)
    	N = len(A)
    	# B^2 + C^2 = A^2
    	for ia in range(N):
    	    target = A[ia]**2
    	    ib, ic = ia+1, N-1
    	    
    	    while ib < ic:
    	        total = A[ib]**2 + A[ic]**2
    	        
    	        if total > target:
    	            ib += 1
    	        elif total < target:
    	            ic -= 1
    	        else:
    	            return True
    	        
    	return False