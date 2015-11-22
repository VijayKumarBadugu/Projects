#Given two strings, determine if one is a permutation of the other.
def permutation(A,B):
	if len(A)!=len(B):
		print 'not an anagram'
		return
	for i in range(len(A)):
		if A[i]!=B[i]:
			print 'not an anagram'
			return
	print ' anagram'
	return
	
string_1	=	'vijay'
string_2	=	'kumar'
string_1	= 	list(string_1)
string_2	= 	list(string_2)
string_1.sort()
string_2.sort()
permutation(string_1,string_2)

