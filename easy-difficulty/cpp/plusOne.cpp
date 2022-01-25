#include <vector>
#include <stdio.h>
#include <iostream>

using namespace std;
class Solution
{
public:
    vector<int> plusOne(vector<int> &digits)
    {
        int size = digits.size();
        bool all_nines = false;

        for (int i = size - 1; i >= 0; i--)
        {
            if (digits[i] == 9)
            {
                digits[i] = 0;
            }
            else
            {
                digits[i]++;
                return digits;
            }
        }

        
            digits[0] = 1;
            for (int i = 1; i < size; i++)
            {
                digits[i] = 0;
            }
            digits.push_back(0);
        

        return digits;
    }
};

int main() {
    Solution run;
    vector<int> num{9}; 
    vector<int> boi = run.plusOne(num);

    for(int i = 0; i < boi.size(); i++) {
        cout << boi[i];
    }

}