#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> arr(n);
    int sum = 0;
    for(int i = 0; i<n; i++){
        cin>>arr[i];
        sum = sum + arr[i];
    }
    cout<<(double)sum/n;

    return 0;
}