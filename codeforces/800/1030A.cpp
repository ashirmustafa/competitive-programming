#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    bool is_hard = false;
    vector<int> values(n);

    for (int i = 0; i < n; i++) {
        cin >> values[i];
        if(values[i] == 1){
            is_hard = true;
        }
    }
    if(is_hard == true){
        cout<<"HARD";
    }
    else{
        cout<<"EASY";
    }
    

    return 0;
}
