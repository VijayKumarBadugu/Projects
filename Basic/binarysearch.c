#include<stdio.h>
binarySearch(int arr[], int start, int end, int element)
{
	int middle;
	while(start<=end)
	{
		middle=(start+end)/2;
		if(arr[middle]==element)
		{
			return middle;
		}
		else
		{
			if(arr[middle]<element)
			{
				start 	=middle+1;
			}
			else
			{
				end	=middle-1;
			}
		}
	}
	return -1;
}
int main(void)
{
   int arr[] = {2, 3, 4, 10, 40};
   int n = sizeof(arr)/ sizeof(arr[0]);
   int x = 12;
   int result = binarySearch(arr, 0, n-1, x);
   (result == -1)? printf("Element is not present in array")
                 : printf("Element is present at index %d", result);
   return 0;
}
