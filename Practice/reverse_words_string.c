#include<stdio.h>
#include<string.h>
void reverse_word(char str[],int start,int end)
{
	char t;
	while(start<end)
	{
		t 		=	str[start];
		str[start]	=	str[end];
		str[end]	=	t;
		start++;
		end--;
	}
}
void reverse_sentence(char str[])
{
	int len	= strlen(str);
	int start = 0;
	int i;
	for(i=1;i<len;i++)
	{
		if(str[i]==' ')
		{
			reverse_word(str,start,i-1);
			start	= i+1;
		}
	}
	reverse_word(str,start,i-1);
	reverse_word(str,0,len-1);
}


main()
{
	char str[]= " My name is vijay";
	printf("before  %s \n",str);
	reverse_sentence(str);
	printf("after  %s \n",str);
}
