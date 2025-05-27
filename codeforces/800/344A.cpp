#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin>>n;
    int count = 0;
    string* magnets = new string[n];
    for (int i = 0; i < n; i++){
        cin>>magnets[i];
    }
    for (int i = 0; i < n - 1; i++){
        string copy = magnets[i + 1];
        reverse(copy.begin(), copy.end());
        
        if (magnets[i] == copy ){
            count++;
        }
    }
    delete[] magnets;
    cout<<count + 1;
    return 0;
}