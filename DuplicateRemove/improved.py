# don't use any library functions
# don't use any temp data structures
# remove the duplicates in the in_arr
#in_arr = [2,2,2,2,2,2,2,2,3,3,3,3,5,5,5,5,3,3,3,3] 
in_arr = [1,2,3,4,5,2,2,33,4,5]
#in_arr = [1,2,3,4,5,33]
#performs in n2
	  
count	=	1
i	=	1
LEN	=	len(in_arr)
while(i<LEN):
	status	= 0
	for j in range(0,count):
		if(in_arr[i]==in_arr[j]):
			status	=	1
	if(status==0):
		in_arr[count]	=	in_arr[i]
		count		= 	count+1
	i = i+1
print in_arr[0:count]
			

