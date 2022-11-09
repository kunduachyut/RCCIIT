#include <stdio.h>
// Function to recursively search an element in an array
int recursiveSearch(int arr[], int left, int right, int elementToBeSearched)
{
 if (right < left)
 {
 return -1;
 }
 if (arr[left] == elementToBeSearched)
 {
 return left;
 }
 if (arr[right] == elementToBeSearched)
 {
 return right;
 }
 return recursiveSearch(arr, left + 1, right - 1, elementToBeSearched);
}
void printArrayElements(int arr[], int size)
{
 for(int i=0; i<size; i++)
 {
 printf("%d ", arr[i]);
 }
 printf("/n");
}
int main()
{
 int arr1[] = {1, 2, 3, 4, 5, 6, 7};
 int size1 = sizeof(arr1)/sizeof(arr1[0]);
 printf("Array 1: /n");
 printArrayElements(arr1, size1);
 int elementToBeSearched1 = 4;
 printf("Element to be searched: %d /n", elementToBeSearched1);
 int indexOfElement1 = recursiveSearch(arr1, 0, size1-1, elementToBeSearched1);
 if(indexOfElement1 == -1)
 {
 printf("Element %d not found /n", elementToBeSearched1);
 }
 else
 {
 printf("Element %d found at index %d /n", elementToBeSearched1, indexOfElement1);
 }
int arr2[] = {2, 4, 6, 10, 12, 3, 6};
 int size2 = sizeof(arr2)/sizeof(arr2[0]);
 printf("Array 2: /n");
 printArrayElements(arr2, size2);
 int elementToBeSearched2 = 4;
 printf("Element to be searched: %d /n", elementToBeSearched2);
 int indexOfElement2 = recursiveSearch(arr2, 0, size2-1, elementToBeSearched2);
 if(indexOfElement2 == -1)
 {
 printf("Element %d not found /n", elementToBeSearched2);
 }
 else
 {
 printf("Element %d found at index %d /n", elementToBeSearched2, indexOfElement2);
 }
int arr3[] = {1, 1, 1, 1, 1};
 int size3 = sizeof(arr3)/sizeof(arr3[0]);
 printf("Array 3: /n");
 printArrayElements(arr3, size3);
 int elementToBeSearched3 = 2;
 printf("Element to be searched: %d /n", elementToBeSearched3);
 int indexOfElement3 = recursiveSearch(arr3, 0, size3-1, elementToBeSearched3);
 if(indexOfElement3 == -1)
 {
 printf("Element %d not found /n", elementToBeSearched3);
 }
 else
 {
 printf("Element %d found at index %d /n", elementToBeSearched3, indexOfElement3);
 }
 return 0;
}