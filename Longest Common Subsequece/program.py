def Recursion(a,b):
	LA=len(a)
	LB=len(b)
	if(LA==0):
		return 0
	if(LB==0):
		return 0
	if(a[LA-1]==b[LB-1]):
		return 1+Recursion(a[0:LA-1],b[0:LB-1])
	else:
		return max(Recursion(a[0:LA],b[0:LB-1]),Recursion(a[0:LA-1],b[0:LB]))
	


A	=	"ABCDGH"
B	=	"AEDFHR"
print Recursion(A,B)
