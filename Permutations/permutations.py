# printing permutations of string
def permutations(string,i,j):
	if i==j:
		print string
		return

	for k in range(i,j+1):
		
		m		=	string[i]
		string[i]	=	string[k]
		string[k]	=	m
		
		
		permutations(string,i+1,j)
		m		=	string[i]
		string[i]	=	string[k]
		string[k]	=	m
		
	
string	= "abc"

permutations(list(string),0,len(string)-1)
