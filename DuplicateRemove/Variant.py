# don't use any library functions
# don't use any temp data structures
# remove the duplicates in the in_arr
#in_arr = [2,2,2,2,2,2,2,2] 
in_arr = [1,2,3,4,5,2,2,33,4,5]
#in_arr = [1,2,3,4,5,33]
for i in range(1,len(in_arr)):
	j=0
	while(j<i):


		if(i==len(in_arr)):
			break
		if(in_arr[i]==in_arr[j]):
			
			in_arr=in_arr[0:i]+in_arr[i+1:len(in_arr)]
			j=j-1
		j=j+1
		if(i==len(in_arr)):
			break
		
	if(i==len(in_arr)):
		break
print in_arr
