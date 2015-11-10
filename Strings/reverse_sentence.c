#include<stdio.h>
void reverse(char *srt,char *end)
{
	char temp;
	while(srt<end)
	{
		temp	=	*srt;
		*srt	=	*end;
		*end	=	temp;
		srt++;
		end--;
	}
}
void reverseWords(char *s)
{
	char *start	= s;
	char *temp	= s;
	while(*temp)
	{
		*temp++;
		if(*temp=='\0')
		{
			reverse(start,temp-1);
			break;
		}
		else
		{
			if(*temp==' ')
			{
				reverse(start,temp-1);
				start	= temp+1;
			}
		}
		
		
	}
	reverse(s,temp-1);
}


int main()
{
  char s[] = "i like this program very much";
  printf("%s\n", s);
  char *temp = s;
  reverseWords(s);
  printf("%s\n", s);
  getchar();
  return 0;
}
