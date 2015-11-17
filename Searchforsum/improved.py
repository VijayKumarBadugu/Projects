def searchforsum(arr,SUM):
	dicti	= {}
	
		
	for i in arr:
		if(dicti.has_key(SUM-i)):
			print "Numbers exist for sum =" + str(SUM) + " .They are " + str(i)+" ,"+ str(SUM-i)
			return 
		else:
			dicti[i]=1
	print "Numbers doesnt exist"
	
	
arr	=	[1,3,5,100,20,33]
SUM	=	raw_input()
SUM	=	int(SUM)
searchforsum(arr,SUM)
