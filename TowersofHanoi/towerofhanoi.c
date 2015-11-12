#include<stdio.h>
void Tower(int N,char A,char B,char C)
{
	if(N>0)
	{
		Tower(N-1,A,C,B);
		printf(" Move disk %d from %c to %c \n",N,A,C);
		Tower(N-1,B,A,C);
	}
}
main()
{
	int N=1;
	Tower(N,'A','B','C');
}
