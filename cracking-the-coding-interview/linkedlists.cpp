#include <iostream>
using namespace std;

class Node {
public:
  Node* next;
  int data;
  void append(int);
  Node(int d) {
    data = d;
    next = NULL;
  }
};

void Node::append(int a) {
  if(next) {
    next->append(a);
  } else {
    Node newNode(a);
    next = &newNode;
  }
}

int main() {
  Node a(1), b(2);
  cout << a.data << endl;
  a.next = &b;
  cout << b.data << endl;
  cout << a.next->data << endl;

  a.append(3);
  b.append(3);
  cout << b.next->data << endl;

  return 0;
}
