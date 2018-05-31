/*
https://www.geeksforgeeks.org/pentatope-number/
Given a number n, find the nth Pentatope number. A pentatope number is
represented by the fifth number in any row of Pascal’s Triangle. As it is fifth number,
it should start from row having at least 5 numbers. So, it starts from row 1 4 6 4 1.
The formula for the nth pentatopic number is: n (n+1) (n+2) (n+3) / 24

Starting Pentatope numbers are : 1, 5, 15, 35, 70, 126, 210, 330, 495…..
*/
#include <iostream>
using namespace std;

int N = 5;

void pascale(int n) {
  // std::vector<int> array(10);
  for (size_t i = 0; i < n; i++) {
    cout << i << endl;
  }
}

int main() {
  // int result = N * (N + 1) * (N + 2) * (N + 3) / 24;
  // std::cout << result << endl;
  // pascale(5);
  enum color { red, green = 5, blue } c;
  std::cout << c.first << endl;
  return 0;
}
