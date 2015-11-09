#include<stdio.h>
#include<string.h>
#include <stdbool.h>
//reverse strings without effecting special characters
bool isAlphabet(char x)
{
    if ( (x >= 'A' &&  x <= 'Z') || (x >= 'a' &&  x <= 'z') )
	{	
		return true;
	}
	else
	{
		return false;
	}
}

void reverse(char str[])
{
	int len=strlen(str)-1;
	int left	=	0;
	int right	=	len;
	while(left<right)
	{
		if(isAlphabet(str[left])==false)
		{
			left=left+1;
		}
		else
		{
			if(isAlphabet(str[right])==false)
			{
				right=right-1;
			}
			else
			{
				char temp;
				temp		= 	str[left];
				str[left]	=	str[right];
				str[right]	=	temp;
				left=left+1;
				right=right-1;
			}
		}
	}
}

int main()
{
    char str[] = "a!!!b.c.d,e'f,ghi";
   printf("%s\n", str);
    reverse(str);
   printf("%s\n", str);;
    return 0;
}
