#include<stdio.h>
#include<string.h>

int compare (const void * a, const void * b)
{
   return ( *(int*)a - *(int*)b );
}
main()
{
	char *A	="geek";
	char *B	="geeks";
	int lenA 	= strlen(A);
	int lenB	= strlen(B);
	int Array[lenA+1][lenB+1];
	int i,j;
	for(i=0;i<lenA+1;i++)
	{
		for(j=0;j<lenB+1;j++)
		{
			Array[i][j]=0;
		}
	}
	Array[0][0]=0;
	int MAXi[3];
	for(i=1;i<lenA+1;i++)
	{
		Array[i][0]=i;
	}
	for(i=1;i<lenB+1;i++)
	{
		Array[0][i]=i;
	}
	for(i=1;i<lenA+1;i++)
	{
		for(j=1;j<lenB+1;j++)
		{
			if(A[i-1]==B[j-1])
			{
				Array[i][j]=Array[i-1][j-1];
			}
			else
			{	MAXi[0]=Array[i-1][j-1];
				MAXi[1]=Array[i-1][j];
				MAXi[2]=Array[i][j-1];
				//printf(" Vijay the answer is %d %d %d \n",MAXi[0],MAXi[1],MAXi[2]);
				qsort (MAXi, 3, sizeof(int), compare);
				//printf(" Vijay the selected is %d \n",MAXi[0]);
				Array[i][j]=1+MAXi[0];
			}
		}
	}
	printf(" Vijay the answer is %d \n",Array[lenA][lenB]);
	
	
}
