def NumberofIncreasingSubsequence(a,b):
	Cont=[]
	for i in range(b):
		Cont.append(1)
	
	for i in range(1,b):
		for j in range(0,i):
			
			if (a[j]<a[i]):
				if( Cont[i]<Cont[j]+1) :
				
					Cont[i]=Cont[j]+1

	print (max(Cont))
			



a=[10, 22, 9, 33, 21, 50, 41, 60, 80]
b=len(a)
NumberofIncreasingSubsequence(a,b)

