#include<stdio.h>
#include<string.h>

main()
{
	char *B	="AGGTAB";
	char *A	="GXTXAYB";
	int AS	=strlen(A);
	int BS	=strlen(B);
	int max=0;
	
	int Array[AS][BS];
	int i,j;
	for(i=0;i<AS+1;i++)
	{
		for(j=0;j<BS+1;j++)
		{
			Array[i][j]=0;
		}
	}
	
	for(i=1;i<AS+1;i++)
	{
		for(j=1;j<BS+1;j++)
		{
			if(A[i-1]==B[j-1])	
			{
				Array[i][j]=Array[i-1][j-1]+1;
			}
			else
			{
				if(Array[i][j-1]>Array[i-1][j])
				{
					Array[i][j]=Array[i][j-1];
				}
				else
				{
					Array[i][j]=Array[i-1][j];
				}
			}
			if(Array[i][j]>max)
			{
				
				max=Array[i][j];
			}
			//printf("sum=%d i=%d j=%d a=%c b=%c\n",Array[i][j],i,j,A[i-1],B[j-1]);
		}
	}
	printf("Final is %d\n",max);
}
