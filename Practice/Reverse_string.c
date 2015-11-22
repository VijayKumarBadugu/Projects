//Reverse a string.

#include<stdio.h>
#include<string.h>
main()
{
	char str[]	= "vi";
	int i;
	char t;
	int len	= strlen(str);
	printf("before is %s \n",str);
	for(i=0;i<len/2;i++)
	{
		t		=	str[i];
		str[i]		=	str[len-1-i];
		str[len-1-i]	=	t;
	}
	printf("reversed is %s \n\n",str);
}
