// Online C++ compiler to run C++ program online
// Print the below Pattern
/*

1 2 3 4 5 5 4 3 2 1 
1 2 3 4 * * 4 3 2 1
1 2 3 * * * * 3 2 1
1 2 * * * * * * 2 1
1 * * * * * * * * 1

*/
#include <iostream>
using namespace std;

int main() {
    
    int n;
    cin>> n;
    int row=1, col=1;

    // Print the 1st Triangle
    while (row <= n)
    {
        col = 1;
        while(col<=n-row+1)
        {
            cout<<col;
            col = col + 1;
        }

    // Print the stars
    int stars = (2 * row) - 2;
    while(stars)
    {
        cout<<"*";
        stars = stars - 1;
        
    }
    
    // Print the 2nd Triangle
        
    col = n - row + 1;
    while (col >= 1) {
        cout << col;
        col--;
    }
        
    cout<< endl;
    row = row +1;
        
    }
    
    return 0;
}