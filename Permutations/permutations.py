def permutations(string,i,j):
	print string
	for k in range(i+1,j+1):
		
		m		=	string[i]
		string[i]	=	string[k]
		string[k]	=	m
		
		
		permutations(string,i+1,j)
		m		=	string[i]
		string[i]	=	string[k]
		string[k]	=	m
		
	
string	= "abc"

permutations(string,0,len(string)-1)
