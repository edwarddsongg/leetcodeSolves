
void reverse(int arr[], int start, int end) {
    while(start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        
        ++start;
        --end;
    }
}


void rotate(int arr[], int numsSize, int k){
    if(k == numsSize || numsSize == 1) {
        return;
    }
    
    if(k > numsSize) {
        k=k%numsSize;
    }
    reverse(arr, 0, numsSize-1);
    reverse(arr, 0, k-1);
    reverse(arr, k, numsSize-1);
}