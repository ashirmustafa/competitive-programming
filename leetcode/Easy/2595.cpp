#include <vector>
using namespace std;

class Solution {
public:
    vector<int> evenOddBit(int n) {
        int index = 0;
        int count_even = 0;
        int count_odd = 0;

        while (n > 0) {
            int bit = n % 2;
            if (bit == 1) {
                if (index % 2 == 0) {
                    count_even += 1;
                } else {
                    count_odd += 1;
                }
            }
            n = n / 2;
            index += 1;
        }

        return {count_even, count_odd};
    }
};
