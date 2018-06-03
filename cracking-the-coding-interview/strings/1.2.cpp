// 1 2 Write code to reverse a C-Style String
// (C-String means that “abcd” is represented as five characters, including the null character )
#include <iostream>
using namespace std;

void reverse(char *string) {
  char *end = string;
  while (*end) {
    end++; // Move end ptr
  }
  end--; // Back from null ptr
  while (end > string) {
    char tmp = *string;
    *string = *end;
    *end = tmp;
    string++;
    end--;
  }
}

int main() {
  char s[] = {'h','i', '\0'};
  cout << s << endl;
  reverse(s);
  cout << s << endl;
}
