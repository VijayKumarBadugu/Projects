def Recursion(a,b):
	LA=len(a)
	LB=len(b)
	if(LA==0):
		return -1
	if(LB==0):
		return -1
	if(a[LA-1]==b[LB-1]):
		Temp=Recursion(a[0:LA-1],b[0:LB-1])
		if((Temp)!=-1):
			return str(a[LA-1])+str(Recursion(a[0:LA-1],b[0:LB-1]))
		else:
			return str(a[LA-1])
		
			
			
			
	else:
		Temp1	= 	Recursion(a[0:LA],b[0:LB-1])
		Temp2	=	Recursion(a[0:LA-1],b[0:LB])
		#print Temp1,Temp2
		 
		if(Temp1==-1 and Temp2==-1):
			return -1
		else:
			Temp1=str(Temp1)
			Temp2=str(Temp2)
			
			if((Temp1)=="-1"):
				
				return str(Temp2)
			if((Temp2)=="-1"):
				
				return str(Temp1)
			if(len(Temp1)>len(Temp2)):
				
				return str(Temp1)
				
			else:
				
				return str(Temp2)
				
				
A	=	"ABCDGH"
B	=	"AEDFHR"
C	=	"AGGTAB" 
D	=	"GXTXAYB"
Temp= Recursion(A,B)
print Temp[::-1]
		
		
				
