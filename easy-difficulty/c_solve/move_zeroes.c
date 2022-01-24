#include <stdlib.h>
#include <stdio.h>

void moveZeroes(int* nums, int numsSize){
    int l = numsSize;
    int non_zero = 0;
    for(int i = 0; i < l; i++) {
        if(nums[i]!=0)
        nums[non_zero++] = nums[i];
    }

    while(non_zero < numsSize) {
        nums[non_zero++] = 0;
    }
}