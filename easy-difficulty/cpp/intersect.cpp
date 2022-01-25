#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        int count = 0;
        for(int i = 0; i < nums1.size(); i++) {
            for(int k = 0; k < nums2.size(); i++) {
                if(nums1[i] == nums2[k]) {
                    nums2.erase(nums2.begin()+k);
                    nums1[count++] = nums1[i];
                    k = 0;
                }
            }
        }

        for(int i = 0; i < nums2.size(); i++) {
            cout << nums2[i] << endl;
        }

        nums1.erase(nums1.begin()+ count, nums1.begin() + nums1.size());
        return nums1;
    }
};

int main() {
    Solution run;
    vector<int> boi{4, 9, 5};
    vector<int> boi1{9,4,9,8,4};
    vector<int> inter = run.intersect(boi, boi1);

    for(int i = 0; i < inter.size(); i++) {
        cout << inter[i] << " ";
    }
}