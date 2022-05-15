# include <iostream>
using namespace std;

void pointer(int x, int &y, int *z) {
    x = 11;
    y = 12;
    *z = 13;
}

int main() {
    // double num = 3.14;
    // double *ptr;
    // ptr = &num;
    // cout << ptr << '\n';
    // cout << &num << '\n';
    // cout << *ptr << '\n';
    // cout << num << '\n';

    int a = 3;
    int b = 4;
    int c = 5;

    pointer(a, b, &c);

    cout << "a: " << a << '\n';
    cout << "b: " << b << '\n';
    cout << "c: " << c << '\n';
    
    return 0;
}