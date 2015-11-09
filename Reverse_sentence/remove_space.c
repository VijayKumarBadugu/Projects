#include<stdio.h>
#include<string.h>
//remove spaces in string
void removeSpaces(char s[])
{
	int len	=	strlen(s);
	int i,count;
	count=0;
	char *temp;
	temp	= 	s;
	while(*temp!='\0')
	{
		if(*temp!=' ')
		{
			s[count]	=	*temp;
			count	=	count+1;
		}
		*temp++;
	}
	s[count]='\0';
}
int main()
{
    char str[] = "g  eeks     for ge  eeks  ";
	  printf("%s\n", str);
    removeSpaces(str);
	  printf("%s\n", str);
    
    return 0;
}
