// Online C++ compiler to run C++ program online
// Print the following pattern
// * * * * 
// * * *
// * *
// *

#include <iostream>
using namespace std;

int main() {
    
    int n;
    cin>> n;
    int row, col;
    
    row = 1;
    
    while(row<=n)
    {
        col = 1;
       while(col<=n - row +1)
       {
           
           cout<<"*";
           col = col +1;
       }
        cout << endl;
        row = row +1;

    }

    return 0;
}