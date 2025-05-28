#include <iostream>
#include <cmath>
using namespace std;

int main() {
    long long n;
    cin >> n;

    long long total = (long long)ceil((double)n / 2);

    if (n % 2 == 0) {
        cout << total;
    } else {
        cout << -total;
    }

    return 0;
}
