//Determine if string has all unique characters. Next, don't use any additional data structures.

#include<stdio.h>
#include<string.h>
main()
{
	char *str 	= 	"vv";
	int len	= strlen(str);
	printf(" length is %d \n",len);
	int i,j;
	int status=0;
	for(i=1;i<len;i++)
	{
		for(j=0;j<i;j++)
		{
			if(str[i]==str[j])
			{
				status =1;
				printf(" Duplicates exist \n");
			}
		}
	}
	if(status==0)
	{
		printf("Duplicates doesnt exist \n");
	}
	
}
