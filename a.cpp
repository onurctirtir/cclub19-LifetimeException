#include <iostream>
#include <list>

int main() {
    std::list<char> s;
    auto it = s.begin();

    std::string input;

    std::getline(std::cin, input);

    for (char c : input) {

        if (c == '[') {
            it = s.begin();
        }
        else if (c == ']') {
            it = s.end();
        }
        else {
            if (it != s.end()) {
                std::next(it);
            }

            if (it == s.end()) {
                s.push_back(c);
                it = s.end();
            }
            else {
                s.insert(it, c);
            }
        }
    }

    for (char it : s) {
        std::cout << it;
    }
    std::cout << std::endl;

    return 0;
}
