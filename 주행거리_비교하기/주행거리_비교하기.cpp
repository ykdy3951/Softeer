#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int a, b;
    cin >> a >> b;
    if (a > b) 
        cout << "A";
    else if (b > a)
        cout << "B";
    else
        cout << "same";
    return 0;
}