#include<stdio.h>
#include<string.h>
//String Reversal
void reverse(char s[])
{
	int end	= strlen(s)-1;
	int start	=	0;
	char tmp;
	while(start<end)
	{
		tmp	=	s[start];
		s[start]=	s[end];
		s[end]	=	tmp;
		start++;
		end--;
		
	}
}
int main()
{
    char str[] = "Vijay";
   printf("%s\n", str);
    reverse(str);
   printf("%s\n", str);;
    return 0;
}
