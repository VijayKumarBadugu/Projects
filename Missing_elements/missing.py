List	=[88, 105, 3, 2, 200, 0, 10]
List	=sorted(List)
start	=	0
end	=	0
curr	=	0
for i in range(len(List)):
	if start!=List[i] and i==0:
		print '0',"-",List[i]-1
		start	=	List[i]+1
	if start!=List[i] and List[i]<100:
		print start,"-",List[i]-1
		start	=	List[i]+1
	
	
	

