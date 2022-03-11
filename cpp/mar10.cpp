#include <iostream>

int doubleNumber(int x) {
    return x * 2;
}

int main() {
    std::cout << "Enter a Number: ";
    int num{};
    std::cin >> num;
    std::cout << doubleNumber(num) << "\n";
    return 0;
}