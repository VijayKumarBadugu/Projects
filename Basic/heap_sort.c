#include<stdio.h>
void swap(int *a,int *b)
{
	int t;
	t	=	*a;
	*a	=	*b;
	*b	=	t;
}
void heapify(int *arr,int pivot,int size)
{
	int left;
	int right;
	int largest;
	left	=	2*pivot+1;
	right	=	left+1;
	largest	=	pivot;
	if(left<size && arr[left]>arr[pivot])	//REM
	{
		largest	=	left;
	}
	
	if(right<size && arr[right]>arr[largest])	//REM
	{
		largest	=	right;
	}
	if(pivot==largest)
	{
		return;
	}
	else
	{
		swap(&arr[largest],&arr[pivot]);
		heapify(arr,largest,size);
	}
	
}
	

void build_heap(int *arr,int size)
{
	int i;
	i	=	size/2;
	while(i>=0)
	{
		heapify(arr,i,size);
		i=i-1;
	}
}
void heapSort(int *arr,int size)
{
	build_heap(arr,size);
	while(size>0)
	{
		heapify(arr,0,size);
		swap(&arr[0],&arr[size-1]);
		size=size-1;
	}
	
}
void printArray(int* arr, int size)
{
    int i;
    for (i = 0; i < size; i++)
        printf("%d ", arr[i]);
}

int main()
{
    int arr[] = {12, 11, 13, 5, 6, 7};
    int size = sizeof(arr)/sizeof(arr[0]);

    printf("Given array is \n");
    printArray(arr, size);
	
    heapSort(arr, size);

    printf("\nSorted array is \n");
    printArray(arr, size);
    return 0;
}
