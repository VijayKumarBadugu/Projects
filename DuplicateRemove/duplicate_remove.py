# don't use any library functions
# don't use any temp data structures
# remove the duplicates in the in_arr 
in_arr = [2,2,2,2,2,2,2]
#in_arr = [1,2,3,4,5,33]


for i in range(len(in_arr)):
	j=i+1
	while(j<len(in_arr)):
		
		
		if j==len(in_arr):
			break

		if(in_arr[i]==in_arr[j]):
			
			print "removing",in_arr[j]
			in_arr = in_arr[0:j]+in_arr[j+1:len(in_arr)]
			j=j-1
		j=j+1
print in_arr
			
			
		
	
