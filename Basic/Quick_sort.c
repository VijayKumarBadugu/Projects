#include<stdio.h>
void swap(int *a,int *b)
{
	int t;
	t	=	*a;
	*a	=	*b;
	*b	=	t;
}
int partition(int *arr,int start,int end)
{
	int key;
	key	=	arr[end];
	int i	= 	start;
	int j	= 	start;
	while(j<end)
	{
		//printf("i=%d j=%d end=%d\n",i,j,end);
		if(arr[j]<=key)
		{
			//printf("Swapping %d with %d \n",arr[i],arr[j]);
			swap(&arr[j],&arr[i]);
			i=i+1;
		}
		j=j+1;
	}
	swap(&arr[end],&arr[i]);
	//printf(" arr[M]=%d position is %d \n",arr[i],i);
	return i;
	
}

void quickSort(int *arr,int start,int end)
{
	if(start<end)
	{
		int middle	=	partition(arr,start,end);
		
		//printf("Vijay start=%d middle=%d end=%d\n",start,middle,end);
		
		quickSort(arr,start,middle-1);
		quickSort(arr,middle+1,end);
	}
}
void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}
 

int main()
{
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr)/sizeof(arr[0]);
    printArray(arr, n);
    quickSort(arr, 0, n-1);
    printf("Sorted array: \n");
    printArray(arr, n);
    return 0;
}
