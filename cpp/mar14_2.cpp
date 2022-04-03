# include <iostream>

int readNumber() {
    std::cout << "Enter a number: ";
    int x{};
    std::cin >> x;
    return x;
};

int writeAnswer(int ans) {
    std::cout << ans;
};
