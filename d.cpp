#include <iostream>
#include <list>
#include <vector>
#include <cstring>

const long NMAX = 10000+1;
std::vector<long> board[NMAX];
bool notEmpty[NMAX];

int main() {
    memset(notEmpty, 0, NMAX * sizeof(bool));

    long N;
    std::cin >> N;

    long dimX = -1;

    for (long i = 0; i < N; i++) {

        long x, y;
        std::cin >> x >> y;

        notEmpty[x] = true;

        board[x].push_back(y);

        dimX = std::max(x, dimX);
    }

    long maxScore = 0;

    for (long r = 1; r <= dimX; r++) {
        long curScore = 0;

        for (long x = 1; x <= dimX; x++) {
            if (notEmpty[x]) {
                for (long y : board[x]) {
                    if (y >= std::abs(r-x) ) {
                        curScore += 1;
                    }
                }
            }
        }

        maxScore = std::max(maxScore, curScore);
    }

    std::cout << maxScore << std::endl;

    return 0;
}
