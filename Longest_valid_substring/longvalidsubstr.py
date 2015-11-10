string = "((()()"
string2 = "()(()))))"
left	=	0
right	=	0
count	=	0
for i in string2:
	if(i=='('):
		left=left+1
	if(i==')'):
		right=right+1
	if(left>0 and right>0):
		left=left-1
		right=right-1
		count	=	count+1
	if(left==0 and right>0):
		
		right=0
print count*2
