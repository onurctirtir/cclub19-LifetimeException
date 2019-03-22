#include <iostream>
#include <vector>
#include <cstdlib>
#include <iomanip>

int main(){


  long long int N, L, T;

  std::cin >> N >> L;

  std::vector<long long int> v_Vector(L);

  for(long long int i  = 0; i < L ; i++){

    long long int temp;
    std::cin >> temp;
    v_Vector[i] = abs(temp);
  }

  std::cin >> T;

  double res = 1.0;

  std::cout << std::fixed;
  std::cout << std::setprecision(8);


  for(long long int i = 0; i < L; i++){

      if(v_Vector[i] * T >= N){
        std::cout << 1;
        return 0;
      }
      res =  (double(N) - double(v_Vector[i]) * double(T)) / double(N) * res;
  }

  std::cout << (1 - res);

  return 0;
}
