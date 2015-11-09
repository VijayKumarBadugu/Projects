#include<stdio.h>
void printArray(int arr[], int n)
{
   int i;
   for (i=0; i < n; i++)
       printf("%d ", arr[i]);
   printf("\n");
}

insertionSort(int arr[],int n)
{
	int i;
	int j;
	int key;
	for(i=1;i<n;i++)
	{
		key	=	arr[i];
		j=i-1;
		while(j>=0)
		{
			if(arr[j]>key)
			{
				arr[j+1]	=	arr[j];
			}
			else
			{
				
				break;
			}
			j=j-1;
			printArray(arr, n);
		}
		arr[j+1]		=	key;
	}
}
int main()
{
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr)/sizeof(arr[0]);
 
	printArray(arr, n);
	printf("\n");
    insertionSort(arr, n);
    printArray(arr, n);
 
    return 0;
}
