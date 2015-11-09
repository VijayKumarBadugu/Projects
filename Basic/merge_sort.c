#include<stdio.h>
void printArray(int A[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}

void mergeCombine(int *arr,int start,int middle,int end)
{
	int l_size	=	middle-start+1;
	int r_size	=	end-(middle+1)+1;
	int A[l_size];
	int B[r_size];
	int m;
	//printf("Start = %d middle = %d end = %d \n",start,middle,end);
	for(m=0;m<l_size;m++)
	{
		A[m]	=	arr[m+start];
		//printf(" A[%d] = %d  \n",m+start,A[m]);
	}
	
	for(m=0;m<r_size;m++)
	{
		B[m]	=	arr[m+middle+1];
		//printf(" B[%d] = %d  \n",m+middle+1,B[m]);
	}
	
	int i,j,k;
	k	=	start;
	i	=	0;
	j	=	0;

	
	while(i<l_size && j<r_size)
	{
		if(A[i]<B[j])
		{
			arr[k]	=	A[i];
			i	=	i+1;
			//printf(" A %d\n",arr[k]);
		}
		else
		{
			arr[k]	=	B[j];
			j	=	j+1;
			//printf(" B %d\n",arr[k]);
		}
		k = k+1;
	}

	
	if(i<l_size)
	{
		while(i<l_size)
		{
			
				arr[k]	=	A[i];
				i	=	i+1;
			
				k = k+1;
				//printf(" A %d\n",arr[k]);
		}
	}
	

	if(j<r_size)
	{
		while(j<r_size)
		{
			arr[k]	=	B[j];
			j	=	j+1;
			k = k+1;
			//printf(" B %d\n",arr[k]);
		}
	}
	
	for(i=start;i<=end;i++)
	{
		//printf(" arr[%d] = %d ",i,arr[i]); 
	}
	//printf("\n");
	
}
void mergeSort(int *arr,int start, int end)
{
	int middle;
	if(start<end)
	{
		middle	=	start+((end-start)/2);
		mergeSort(arr,start,middle);
		mergeSort(arr,middle+1,end);
		mergeCombine(arr,start,middle,end);
	}
	
	
}


 
/* Driver program to test above functions */
int main()
{
    int arr[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(arr)/sizeof(arr[0]);
 
    printf("Given array is \n");
    printArray(arr, arr_size);
 
    mergeSort(arr, 0, arr_size - 1);
 
    printf("\nSorted array is \n");
    printArray(arr, arr_size);
    return 0;
}
