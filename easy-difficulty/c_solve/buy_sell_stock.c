#include <stdlib.h>
#include <stdio.h>

int maxProfit(int* prices, int pricesSize){
    int profit = 0;
    for(int i = 0; i < pricesSize-1; i++) {
        if(prices[i+1]-prices[i]>0) {
            profit+=prices[i+1]-prices[i];
        }
    }
    return profit;
}

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    int profit = maxProfit(arr, 5);
    printf("Profit:%d", profit);
}