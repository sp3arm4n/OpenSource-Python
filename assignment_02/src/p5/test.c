#include<stdio.h>

#define true  1
#define false 0

void print_array( int *a, int n) {
    for( int i=0; i<n; i++) 
        printf("%d ", a[i]);
    printf("\n");
}

void insertion(int *a, int n){
    int i, j, move;
    int val;
    
    for(i=1; i<n; i++){
       val = a[i];
       j = i;
       if( a[j-1] > val ) 
          move = true;
       else
          move = false;
       
       while( move ) {
          a[j] = a[j-1];
          j = j - 1;
          if( j >0 && a[j-1] > val )
             move = true;
          else
             move = false;
        }
        a[j] = val;
        print_array( a, n);
    }
}

void bubble(int *a, int n){
    int i, j;
    int val;
    for(i=n-1; i > 0; i--){
        for(j=0; j<i; j++){
            if( a[j] > a[j+1] ) {
                val = a[j];
                a[j] = a[j+1];
                a[j+1] = val;
            }
        }
        print_array( a, n);
    }
}

void selection(int *a, int n){
    int i, j, least;
    int val;

    for(i = 0;  i <n-1; i++){
        least = i;
        for( j = i + 1; j < n; j++)
            if( a[j] < a[least] ) least = j;
        val = a[least];
        a[least] = a[i];
        a[i] = val;
        print_array( a, n);
    }
}


int a[] = { 7, 6, 1, 2, 3, 4, 5 };
int n = 7;

void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int partition (int arr[], int low, int high)
{
    int pivot = arr[high];    // pivot
    int i = (low - 1);  // Index of smaller element

    for (int j = low; j <= high- 1; j++)
    {
        // If current element is smaller than or
        // equal to pivot
        if (arr[j] <= pivot)
        {
            i++;    // increment index of smaller element
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    print_array(a, n);    
    return (i + 1);
}

quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[pi] is now
           at right place */
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Before pi
        quickSort(arr, pi + 1, high); // After pi
    }
}

int main(){
    int a[] = { 7, 6, 1, 2, 3, 4, 5 };
    int n = 7;

    printf("inserstion sort:\n");
    insertion(a, n);

    printf("bubble sort:\n");
    bubble(a, n);

    printf("selection sort:\n");
    selection(a, n);
    
    printf("quick sort:\n");
    quickSort( a, 0, 6);

    return 1;
}
