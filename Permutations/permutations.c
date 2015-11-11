#include<stdio.h>
#include<string.h>

void permuations(char *str,int start,int end)
{
	int i;
	
	char temp;
	if(start==end)
	{
		printf("%s \n",str);
		return;
	}
	
	for(i=start;i<=end;i++)
	{
		temp	=	str[start];

		str[start]	=	str[i];

		str[i]	=	temp;
		
		
		permuations(str,start+1,end);
		
		temp	=	str[start];

		str[start]	=	str[i];

		str[i]	=	temp;
		
		
	}
}
main()
{
	char str[]	=	"abc";
	int k		=	strlen(str);
	printf(" length = %d \n",k-1);
	permuations(str,0,k-1);
}
