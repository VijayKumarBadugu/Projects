#http://www.geeksforgeeks.org/check-if-two-given-strings-are-isomorphic-to-each-other/
def isomorphic(A,B):
	if(len(A)!=len(B)):
		return -1
	Map	=	{}
	Mark	=	{}
	for i in A:
		Map[i]	= -1
	for i in B:
		Mark[i]	= -1
	for i in range(len(A)):
		if(Map[A[i]]==-1):
			
			if(Mark[B[i]]==1):
				
				return -1
			
			Mark[B[i]]	= 1
			
			Map[A[i]]	= B[i]
		else:
			if(Map[A[i]]!=B[i]):
				
				return -1
	return 1
			
		
A = 'abc'
B = 'xzy'
print isomorphic(A,B)
	
