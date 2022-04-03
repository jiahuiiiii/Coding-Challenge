# include <iostream>
# include <string>

int main () {
    std::string myName = "Alex";
    int length = static_cast<int>(myName.length());
    std::cout << length;
    return 0;
}