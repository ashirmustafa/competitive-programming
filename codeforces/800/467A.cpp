#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    int count = 0;  

    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b; 
        if (abs(a - b) >= 2){
            count++;
        }
    }
    cout<<count;

    return 0;
}
