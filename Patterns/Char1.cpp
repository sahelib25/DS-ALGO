// Online C++ compiler to run C++ program online
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
       char start = 'A' + row - 1; // Calculate the first character to be printed in each row
       while(col<=n)
       {
           
           cout<< start;
           start = start + 1;
           col = col +1;
       }
       
       cout << endl;
       row = row + 1;

    }

    return 0;
}