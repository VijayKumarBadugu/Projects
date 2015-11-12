def Tower(N,A,B,C):
	if(N>0):
		Tower(N-1,A,C,B)
		print "Move ",N," from",A," to ",C
		Tower(N-1,B,A,C)
	
N=1
Tower(N,'A','B','C')
