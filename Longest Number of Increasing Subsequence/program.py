GlobalMax=0
def NumberofIncreasingSubsequence(a,b):
	if( b==1):
		#print 1,b
		return 1
	MaxSofar=1

	for j in range(1, b):
		
		res	= NumberofIncreasingSubsequence(a,j)
		if(a[j-1]<a[b-1]):
			if(res+1 >MaxSofar):
				MaxSofar=res+1
	global GlobalMax
	if(GlobalMax<MaxSofar):
		GlobalMax=MaxSofar
	
	#print "vijay",MaxSofar,b
	return MaxSofar
	
a=[10, 22, 9, 33, 21, 50, 41, 60, 80,89,100]
b=len(a)
NumberofIncreasingSubsequence(a,b)
print GlobalMax

