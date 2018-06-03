#include <iostream>
using namespace std;

void memcopy(int* src, int* dst, int N) {
  if (dst > src) {
    dst += N;
    src += N;
  }
  while (N > 0) {
    *dst = *src;
    if (dst > src) {
      src--;
      dst--;
    } else {
      src++;
      dst++;
    }
    N--
  }
}

int main() {
  int c = 1;
  int *a = &c;
  a++;
  *a = 2;
  a++;
  *a = 3;
  a++;
  *a = 4;
  a -= 3;
  int b[4] = {5, 6, 7, 8};
  for (size_t i = 0; i < 4; i++) {
    cout << a[i] << ", ";
    cout << b[i] << ", ";
  }
  cout << endl;
  // memcopy(a, b,  for (size_t i = 0; i < 4; i++) {
    cout << a[i] << ", ";
    cout << b[i] << ", ";
  }
  cout << endl;

}
